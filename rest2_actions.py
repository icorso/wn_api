import datetime
import json
import re
from urllib.parse import urlencode

import six
from faker import Factory

from actions import BaseSource
from data.rest2_payment_requests import rest2_payment_refund, rest2_capture_payment, rest2_payment_reverse, \
    rest2_payment_update
from model import rest2
from model.rest2 import AccessToken, Error, TransactionPaginatedResult, StoreCredentialsRequest, \
    UpdateCredentialsRequest, RefundRequest, Refund
from model.rest2.payment import Payment
from model.rest2.secure_credentials import SecureCredentials

fake = Factory.create()


class Rest2Source(BaseSource):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.url = self._session.url + self._path + '/api/v1'
        self._session.with_headers({'Content-Type': 'application/json', 'Accept': 'application/json'})

    def get_termnal_id(self):
        return self._terminal_id

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,  # noqa: F821
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def deserialize(self, response, response_type):
        """Deserializes response into an object.
        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.
        :return: deserialized object.
        """
        if not 200 <= response.status_code <= 299:
            response_type = "Error"

        # fetch data from response object
        try:
            data = json.loads(response.content.decode('utf-8'))
        except ValueError:
            data = response.data

        return self.__deserialize(data, response_type)

    def __deserialize(self, data, klass):
        """Deserializes dict, list, str into an object.
        :param data: dict, list or str.
        :param klass: class literal, or string of class name.
        :return: object.
        """
        if data is None:
            return None

        if type(klass) == str:
            if klass.startswith('list['):
                sub_kls = re.match(r'list\[(.*)\]', klass).group(1)
                return [self.__deserialize(sub_data, sub_kls)
                        for sub_data in data]

            if klass.startswith('dict('):
                sub_kls = re.match(r'dict\(([^,]*), (.*)\)', klass).group(2)
                return {k: self.__deserialize(v, sub_kls)
                        for k, v in six.iteritems(data)}

            # convert str to class
            if klass in self.NATIVE_TYPES_MAPPING:
                klass = self.NATIVE_TYPES_MAPPING[klass]
            else:
                klass = getattr(rest2, klass)

        if klass in self.PRIMITIVE_TYPES:
            return self.__deserialize_primitive(data, klass)
        elif klass == object:
            return self.__deserialize_object(data)
        elif klass == datetime.date:
            return self.__deserialize_date(data)
        elif klass == datetime.datetime:
            return self.__deserialize_datatime(data)
        else:
            return self.__deserialize_model(data, klass)

    def __deserialize_primitive(self, data, klass):
        """Deserializes string to primitive type.

        :param data: str.
        :param klass: class literal.

        :return: int, long, float, str, bool.
        """
        try:
            return klass(data)
        except UnicodeEncodeError:
            return six.text_type(data)
        except TypeError:
            return data

    def __deserialize_object(self, value):
        """Return a original value.

        :return: object.
        """
        return value

    def __deserialize_date(self, string):
        """Deserializes string to date.

        :param string: str.
        :return: date.
        """
        try:
            from dateutil.parser import parse
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            raise Exception(
                "Failed to parse `{0}` as date object".format(string)
            )

    def __deserialize_datatime(self, string):
        """Deserializes string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        """
        try:
            from dateutil.parser import parse
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            raise Exception("Failed to parse `{0}` as datetime object".format(string))

    def __hasattr(self, object, name):
            return name in object.__class__.__dict__

    def __deserialize_model(self, data, klass):
        """Deserializes list or dict to model.

        :param data: dict, list.
        :param klass: class literal.
        :return: model object.
        """

        if not klass.swagger_types and not self.__hasattr(klass, 'get_real_child_model'):
            return data

        kwargs = {}
        if klass.swagger_types is not None:
            for attr, attr_type in six.iteritems(klass.swagger_types):
                if (data is not None and
                        klass.attribute_map[attr] in data and
                        isinstance(data, (list, dict))):
                    value = data[klass.attribute_map[attr]]
                    kwargs[attr] = self.__deserialize(value, attr_type)

        instance = klass(**kwargs)

        if (isinstance(instance, dict) and
                klass.swagger_types is not None and
                isinstance(data, dict)):
            for key, value in data.items():
                if key not in klass.swagger_types:
                    instance[key] = value
        if self.__hasattr(instance, 'get_real_child_model'):
            klass_name = instance.get_real_child_model(data)
            if klass_name:
                instance = self.__deserialize(data, klass_name)
        return instance

    def authenticate(self, rest2_key=None, silence=True):
        url = self.url + '/account/authenticate'
        response = self._session.with_method('get').with_url(url).with_headers(
            {'Authorization': 'Basic %s' % rest2_key}).request
        access_token = self.deserialize(response, AccessToken)
        if not silence:
            print(url)
            print(access_token.json())
        return access_token

    def payment(self, request, api2_key, silence=True) -> (Payment, Error):
        token = self.authenticate(api2_key, silence=True).token
        url = self.url + '/transaction/payments'
        request.terminal = self._terminal_id
        response = self._session.with_method('post').with_url(url).with_headers(
            {'Authorization': 'Bearer %s' % token}).with_data(request.json()).request
        payment_response = self.deserialize(response, Payment)
        if isinstance(payment_response, Error):
            print("\nERROR OCCURS:\n%s" % payment_response.json())
        if not silence:
            print("\nREQUEST:\n%s\n%s" % (url, request.json()))
            print("\nRESPONSE:\n%s" % payment_response.json())
        return payment_response  # TODO find proper way to union several  

    def get_payment(self, uniqueref, api2_key, silence=True):
        token = self.authenticate(api2_key).token
        url = self.url + '/transaction/payments/%s' % uniqueref
        response = self._session.with_method('get').with_url(url)\
            .with_headers({'Authorization': 'Bearer %s' % token}).request
        payment_response = self.deserialize(response, Payment)
        if not silence:
            print('\nREQUEST: %s\n' % url)
            print('RESPONSE:\n%s\n' % payment_response.json())
        return payment_response

    def payment_refund(self, uniqueref, amount, api2_key, reason=None, operator=None, silence=True):
        token = self.authenticate(api2_key).token
        url = self.url + '/transaction/payments/%s/refunds' % uniqueref
        request = rest2_payment_refund(amount, reason, operator)
        response = self._session.with_method('post').with_url(url).with_headers(
            {'Authorization': 'Bearer %s' % token}).with_data(request.json()).request
        payment_response = self.deserialize(response, Payment)
        if not silence:
            print("REQUEST:\n%s\n%s" % (url, request.json()))
            print("RESPONSE:\n%s" % payment_response.json())
        return payment_response

    def payment_capture(self, uniqueref, api2_key, amount=None, operator=None, silence=True):
        token = self.authenticate(api2_key).token
        url = self.url + '/transaction/payments/%s/capture' % uniqueref
        request = rest2_capture_payment(amount, operator)
        response = self._session.with_method('patch').with_url(url).with_headers(
            {'Authorization': 'Bearer %s' % token}).with_data(request.json()).request
        payment_response = self.deserialize(response, Payment)
        if not silence:
            print("REQUEST:\n%s\n%s" % (url, request.json()))
            print("RESPONSE:\n%s" % payment_response.json())
        return payment_response

    def payment_reverse(self, uniqueref, amount, api2_key, reason=None, operator=None, customer_account=None,
                        silence=True):
        token = self.authenticate(api2_key).token
        url = self.url + '/transaction/payments/%s/reverse' % uniqueref
        request = rest2_payment_reverse(amount, reason, operator, customer_account)
        response = self._session.with_method('patch').with_url(url).with_headers(
            {'Authorization': 'Bearer %s' % token}).with_data(request.json()).request
        reversal_response = self.deserialize(response, Payment)
        if not silence:
            print("REQUEST:\n%s\n%s" % (url, request.json()))
            print("RESPONSE:\n%s" % reversal_response.json())
        return reversal_response

    def payment_update(self, uniqueref, api2_key, request, silence=True):
        token = self.authenticate(api2_key).token
        url = self.url + '/transaction/payments/%s' % uniqueref
        response = self._session.with_method('patch').with_url(url).with_headers(
            {'Authorization': 'Bearer %s' % token}).with_data(request.json()).request
        reversal_response = self.deserialize(response, Payment)
        if not silence:
            print("REQUEST:\n%s\n%s" % (url, request.json()))
            print("RESPONSE:\n%s" % reversal_response.json())
        return reversal_response

    def refund_reverse(self, uniqueref, api2_key, silence=True):
        token = self.authenticate(api2_key).token
        url = self.url + '/transaction/refunds/%s/reverse' % uniqueref
        response = self._session.with_method('patch').with_url(url).with_headers(
            {'Authorization': 'Bearer %s' % token}).request
        reversal_response = self.deserialize(response, Payment)
        if not silence:
            print("REQUEST:\n%s" % url)
            print("RESPONSE:\n%s" % reversal_response.json())
        return reversal_response

    def unreferenced_refund(self, request, api2_key, silence=True) -> (RefundRequest, Error):
        token = self.authenticate(api2_key, silence=True).token
        url = self.url + '/transaction/refunds'
        request.terminal = self._terminal_id
        response = self._session.with_method('post').with_url(url).with_headers(
            {'Authorization': 'Bearer %s' % token}).with_data(request.json()).request
        payment_response = self.deserialize(response, Refund)
        if isinstance(payment_response, Error):
            print("\nERROR OCCURS:\n%s" % payment_response.json())
        if not silence:
            print(token)
            print("\nREQUEST:\n%s\n%s" % (url, request.json()))
            print("\nRESPONSE:\n%s" % payment_response.json())
        return payment_response

    def search(self, api2_key, silence=False, **kwargs):
        token = self.authenticate(api2_key).token
        url = self.url + '/transaction/transactions?'
        url = url + urlencode(kwargs)
        response = self._session.with_method('get').with_url(url).with_headers(
            {'Authorization': 'Bearer %s' % token}).request
        search_response = self.deserialize(response, TransactionPaginatedResult)
        if not silence:
            print("REQUEST:\n%s" % url)
            print("RESPONSE:\n%s" % search_response.json())
        return search_response

    def credentials_store(self, request: StoreCredentialsRequest, api2_key, silence=True) -> (SecureCredentials, Error):
        token = self.authenticate(api2_key, silence=True).token
        url = self.url + '/customer/credentials'
        request.terminal = self._terminal_id
        response = self._session.with_method('post').with_url(url).with_headers(
            {'Authorization': 'Bearer %s' % token}).with_data(request.json()).request
        credentials_response = self.deserialize(response, SecureCredentials)
        if isinstance(credentials_response, Error):
            print("\nREQUEST:\n%s\n%s" % (url, request.json()))
            print("\nERROR OCCURS:\n%s" % credentials_response.json())
        if not silence:
            print("\nREQUEST:\n%s\n%s" % (url, request.json()))
            print("\nRESPONSE:\n%s" % credentials_response.json())
        return credentials_response

    def credentials_update(self, request: UpdateCredentialsRequest, merchant_reference, api2_key, silence=True) -> (SecureCredentials, Error):
        token = self.authenticate(api2_key, silence=True).token
        url = self.url + '/customer/credentials/%s' % merchant_reference
        request.terminal = self._terminal_id
        response = self._session.with_method('patch').with_url(url).with_headers(
            {'Authorization': 'Bearer %s' % token}).with_data(request.json()).request
        credentials_response = self.deserialize(response, SecureCredentials)
        if isinstance(credentials_response, Error):
            print("\nREQUEST:\n%s\n%s" % (url, request.json()))
            print("\nERROR OCCURS:\n%s" % credentials_response.json())
        if not silence:
            print("\nTOKEN:\n%s" % token)
            print("\nREQUEST:\n%s\n%s" % (url, request.json()))
            print("\nRESPONSE:\n%s" % credentials_response.json())
        return credentials_response

