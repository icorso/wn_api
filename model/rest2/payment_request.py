# coding: utf-8

"""
    Merchant API

    # Introduction The Merchant API enables you to connect seamlessly and securely to our [Omni-Channel Payments Platform](https://www.worldnetpayments.com/).  Our APIs are built around [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) principles and [OpenAPI Specification](https://www.openapis.org/) definitions. Complying to such industry standards means that we can offer developers a much better experience by exposing predictable resource-oriented URL's as well as a comprehensive range of HTTP response codes and verbs. Moreover, you have the possibility to enable and take full advantage of [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS) controls to provide out-of-the-box `Discoverability` and `Functional-Awareness` for your integrations.  Get started on building full-featured payment applications and join us in the Revolution of Intelligent Retail.  # Authentication The Merchant API uses a combination of API Keys and [Java Web Tokens (JWT)](https://jwt.io/) to authenticate requests. API Key's hold all the necessary information for issuing JWT access tokens which in turn are required to access protected resources and operations. Therefore, before you can start making any calls, you must generate an API Key and use it to obtain access tokens.  Please, make yourself familiar with the following security schemes before proceeding: <!-- ReDoc-Inject: <security-definitions> --> ## Generating an API Key In order to generate your first API Key you must [sign up](#) for a developer account and follow the steps below: 1. [Log into the SelfCare System](#) with the credentials you received in the welcome email. 2. Under *Settings*, navigate to *API Keys*, and then click the `NEW API KEY` button. 4. Enter an alias and set the permission modes for each Sub-API. 5. Select the terminals that you want the API Key to be allowed to operate. 6. Back on the list, choose the action `View Authentication Key` to be able to see your API Key.  ## Obtaining an Access Token In order to obtain an access token you must use the [authenticate](#operation/authenticate) operation passing your API Key in the `HTTP Authorization` header with `Basic` authentication scheme.  In the snippet below we show how to achieve that using [cURL](https://github.com/curl/curl). However, if you are not familiar with command line tools we recommend [Postman](https://www.getpostman.com/).  ``` curl https://testpayments.worldnettps.com/merchant/api/v1/account/authenticate \\   -H \"Authorization: Basic <Merchant API Key>\" ```  For every successful request you should receive a response just like the one below containing the information associated with your credentials, such as hours to expiry and privileges. Include the JWT Token from the `token` property in the `Authorization` header with `Bearer` authentication scheme for following requests to prove your identity and access protected resources.  ``` {     \"audience\": \"testpayments.worldnettps.com\",     \"boundTo\": \"My API Key\",     \"tokenType\": \"Bearer\",     \"token\": \"<JWT Access Token>\",     \"expiresIn\": 1,     \"enableHypermedia\": true,     \"roles\": [],     \"allowedTerminals\": [] } ```  For security reasons, access tokens expire after a certain amount of time. Therefore, your application must implement a mechanism to keep track of the `expiresIn` property which is the number of hours the token is valid for.  **Note:** The lifespan of a token must not be hard-coded on the client-side as the value of `expiresIn` property is subject to change without prior notice.  ## Making Authenticated Calls Apart from the [authenticate](#operation/authenticate) operation, the entire API requires `Bearer` authentication scheme and expects a valid JWT token as proof of identity. The [cURL](https://github.com/curl/curl) snippet below is an example of how to use your access token, in this specific case, to request the list of available terminals in your account.  ``` curl https://testpayments.worldnettps.com/merchant/api/v1/account/terminals?pageSize=10 \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Bearer <JWT Token>\" ```  **Note:** The API will issue a response with status `401 Unauthorized` for requests carrying an expired JWT.  # API Requests We provide developers looking to integrate with our solutions with a full-featured **Sandbox**.  - Sandbox URL: https://testpayments.worldnettps.com/merchant/  In order to perform actions on the API's resources you must combine your requests with the proper [HTTP Request Method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods).  The Merchant API supports the following HTTP Methods which are sometimes referred as *HTTP Verbs*:  HTTP Method  | Description ------------ | ------------- [GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET) | It requests a representation of the specified resource. Requests using `GET` are read-only. [POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST) | It is used to submit an entity to the specified resource, often causing a change in state on the server. [PATCH](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH) | It is used to apply partial modifications to a resource. [DELETE](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE) | It deletes / cancels / reverts the specified resource.  ## Request Identifiers The Merchant API assigns a unique identifier for every request that comes in. You can find your requests' identifiers either in the `X-Request-Id` header or in the Error field `debugIdentifier`.  Request ID's are part of an effort to speed troubleshooting by facilitating communication between clients and our support team. Since we keep track of all request identifiers in our log files, you just need to inform the request's identifier when asking us to assist you with problems that might come up during your integrations.  ## Customer Account Payloads  Client applications need to be able to send the customers' account details when generating payments, initiating unreferenced refunds and registering secure credentials.  This information is expected in the form of payloads which varies based on the mechanism used to capture the account/card details.  For instance, when the card details are manually inputted, a `KEYED` payload is expected. However, an `EMV` payload is always expected for contact and contactless EMV transactions. It is worth mentioning that the proper use of payloads also depend on the channel over which your terminal is operating. In the table below we show the supported payloads for each of the three available channels:  Channel                      | Supported Payloads ---------------------------- | ------------------------- WEB (eCommerce)              | `KEYED`, `SECURE_CREDENTIALS`, `DIGITAL_WALLET` POS (Cardholder Present)     | `KEYED`, `EMV`, `RAW`, `MAG_STRIPE` MOTO (Mail/Telephone Order)  | `KEYED`, `SECURE_CREDENTIALS`  ## Request Headers HTTP Header  | Description ------------ | ------------- [Accept](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept) | The response format expected by your application.<br />The Merchant API only produces `application/json` response format. [Accept-Language](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language) | It advertises which languages the client is able to understand, and which locale variant is preferred.<br />The Merchant API fully supports English `en` and French `fr` languages. [Content-Type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) | The body format of the request your application is sending to the API.<br />The Merchant API only consumes `application/json` content type. [Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) | It must contain the credentials (API Key or JWT Access Token) to authenticate your application.<br />The API will issue a `401 Unauthorized` response with the `WWW-Authenticate` header attached if your application fails to use this header properly.  ## Partial Updates Partial update requests are signaled with the HTTP method `PATCH`. To perform partial updates, clients must specify only the properties that have changed.  **Note:** To clear the content of a property, supply an empty value.  ## Testing Requests Eventually it will be necessary to perform some transactions. For resources such as testing credit cards and simulated responses, see [Testing Resources](https://docs.worldnettps.com/doku.php?id=developer:integration_docs:testing-guide#testing_resources).  # API Responses Client applications must be able to handle JSON body format as well as a range of [HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) when processing responses. Some resources might also include contextual hypermedia links. We strongly recommend that clients use these links to request more information or perform additional actions on a given resource.  ## HTTP Status Codes The Merchant API has adopted a comprehensive range of status codes where `2XX` statuses are returned for successful requests and `4XX` or `5XX` for failed requests.  The full range of status codes supported by this API:  HTTP Status Code  | Description ----------------- | ------------- [200 OK](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200) | Indicates that the request has succeeded. [201 Created](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/201) | Indicates that the request has succeeded and has led to the creation of a resource. [204 No Content](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/204) | Indicates that the server successfully executed the method but returns no response body.<br />This status is sent specifically to respond to `DELETE` requests. [400 Bad Request](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400) | Indicates that the server cannot or will not process the request due to malformed request syntax or schema violation. [401 Unauthorized](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401) | Indicates that the request has not been applied because it lacks valid authentication credentials.<br />This status is sent with a `WWW-Authenticate` header that contains information on how to authorize correctly. [403 Forbidden](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403) | Indicates that the server understood the request but refuses to authorize it due to the lack of permissions.<br />Re-authenticating will make no difference until the proper permissions and terminals are added to the API Key. [404 Not Found](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404) | Indicates that the server cannot find the requested resource. [405 Method Not Allowed](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/405) | Indicates that the request method is known by the server but is not supported by the target resource. [406 Not Acceptable](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/406) | Indicates that the server cannot produce a response matching the value from `Accept` header. [415 Unsupported Media Type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/415) | Indicates that the server refuses to accept the request because the payload format described by the `Content-Type` is unsupported. [422 Unprocessable Entity](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422) | Indicates that the server understands the content type of the request entity, and the syntax of the request entity is correct, but it was unable to proceed due to semantic errors or failed business validations. [500 Internal Server Error](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) | Indicates that the server encountered an unexpected condition that prevented it from fulfilling the request. [501 Not Implemented](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/501) | Indicates that the server does not yet support the functionality required to fulfill the request, but might in the future.  ## Error Handling In the event of a failure, the Merchant API returns an error response body that includes additional details in the format below:  ``` {     \"debugIdentifier\": \"ae6d75eb-381b-4a01-9f49-fdff12e3848b\",     \"details\": [         {             \"errorCode\": \"X_400_002\",             \"errorMessage\": \"Unable to deserialize value\",             \"source\": {                 \"location\": \"BODY\",                 \"resource\": \"TipType\",                 \"property\": \"type\",                 \"value\": \"VARIABLE\",                 \"expected\": \"Acceptable values: [PERCENTAGE, FIXED_AMOUNT]\"             }         }     ] } ```  Error messages are intended to help developers to fix any problems that may come up during integration.<br />However, if you ever have a hard time troubleshooting an issue or even wish to make a suggestion, do not hesitate to [contact us](https://worldnetpayments.com/contact/). Do not forget to send us the `debugIdentifier` along with your inquiries.  ## HATEOAS (Hypermedia Links) [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS) is a powerful mechanism when it comes to enabling self-discoverability, reducing invalid state transition calls and protecting your application against unexpected changes on resources URL's.  This snippet from a sample `payments` response shows the list of hypermedia controls that represent the operations available for the newly created payment resource.  ``` \"links\": [     {         \"rel\": \"capture\",         \"method\": \"PATCH\"         \"href\": \"https://testpayments.worldnettps.com/merchant/api/v1/transaction/payments/GH2AERQEJS/capture\"     },     {         \"rel\": \"refund\",         \"method\": \"POST\"         \"href\": \"https://testpayments.worldnettps.com/merchant/api/v1/transaction/payments/GH2AERQEJS/refunds\"     },     {         \"rel\": \"update\",         \"method\": \"PATCH\"         \"href\": \"https://testpayments.worldnettps.com/merchant/api/v1/transaction/payments/GH2AERQEJS\"     },     {         \"rel\": \"self\",         \"method\": \"GET\"         \"href\": \"https://testpayments.worldnettps.com/merchant/api/v1/transaction/payments/GH2AERQEJS\"     },     {         \"rel\": \"reverse\",         \"method\": \"DELETE\"         \"href\": \"https://testpayments.worldnettps.com/merchant/api/v1/transaction/payments/GH2AERQEJS\"     } ] ```  # Pagination The Merchant API features a cursor-based pagination which is sometimes referred as continuation token pagination. This pagination approach works by returning a pointer to a specific item in the dataset. On subsequent requests, the server returns results after the given pointer.  Clients don't need to worry about implementing complex pagination mechanism in their applications as we return, for all paginated resources, the total count and a hypermedia link that can be used to load more results. It is important to mention that the response containing the last elements will not contain a `next` hyperlink. We do that so you know that there are no more elements to load. ``` \"links\": [     {         \"rel\": \"next\",         \"method\": \"GET\"         \"href\": \"https://testpayments.worldnettps.com/merchant/api/v1/account/terminals?next=CWY4XRGUUY\"     } ] ```  The default number of elements per page is `10` and the maximum is `100`, but it can be changed by adding the query parameter `pageSize` to requests as follows: ``` curl https://testpayments.worldnettps.com/merchant/api/v1/account/terminals?pageSize=5 \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Bearer <JWT Token>\" ```  **Note:** For performance reasons, the elements inside of a paginated list only represent a compact version of the resource listed. To retrieve the full version of a given resource, client applications must make a subsequent request using the proper hypermedia link.  # Versioning Versioning ensures that changes are backward compatible. The Merchant API uses a major and minor version nomenclature to manage changes.  ## Major Versions Major version numbers will reflect in the REST URL, for example `/api/v1/transaction/payments`.  Currently, **v1** is the only supported major version.  ## Minor Versions Minor and backward-compatible changes will be advertised via `X-API-Version` response header, for example `X-API-Version: 2020-01-01`.  Developers should use this header to keep track of new features and optimizations that might benefit their applications.   # noqa: E501

    OpenAPI spec version: v1
    Contact: support@worldnettps.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class PaymentRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'channel': 'str',
        'terminal': 'str',
        'operator': 'str',
        'order': 'Order',
        'customer': 'Customer',
        'customer_account': 'Payload',
        'credential_on_file': 'CredentialOnFile',
        'ip_address': 'IpAddress',
        'auto_capture': 'bool',
        'process_as_sale': 'bool',
        'offline_processing': 'OfflineProcessing',
        'additional_data_fields': 'list[CustomField]'
    }

    attribute_map = {
        'channel': 'channel',
        'terminal': 'terminal',
        'operator': 'operator',
        'order': 'order',
        'customer': 'customer',
        'customer_account': 'customerAccount',
        'credential_on_file': 'credentialOnFile',
        'ip_address': 'ipAddress',
        'auto_capture': 'autoCapture',
        'process_as_sale': 'processAsSale',
        'offline_processing': 'offlineProcessing',
        'additional_data_fields': 'additionalDataFields'
    }

    def __init__(self, channel=None, terminal=None, operator=None, order=None, customer=None, customer_account=None, credential_on_file=None, ip_address=None, auto_capture=True, process_as_sale=False, offline_processing=None, additional_data_fields=None):  # noqa: E501
        """PaymentRequest - a model defined in Swagger"""  # noqa: E501
        self._channel = None
        self._terminal = None
        self._operator = None
        self._order = None
        self._customer = None
        self._customer_account = None
        self._credential_on_file = None
        self._ip_address = None
        self._auto_capture = None
        self._process_as_sale = None
        self._offline_processing = None
        self._additional_data_fields = None
        self.discriminator = None
        if channel is not None:
            self.channel = channel
        self.terminal = terminal
        if operator is not None:
            self.operator = operator
        self.order = order
        if customer is not None:
            self.customer = customer
        if customer_account is not None:
            self.customer_account = customer_account
        if credential_on_file is not None:
            self.credential_on_file = credential_on_file
        if ip_address is not None:
            self.ip_address = ip_address
        if auto_capture is not None:
            self.auto_capture = auto_capture
        if process_as_sale is not None:
            self.process_as_sale = process_as_sale
        if offline_processing is not None:
            self.offline_processing = offline_processing
        if additional_data_fields is not None:
            self.additional_data_fields = additional_data_fields

    @property
    def channel(self):
        """Gets the channel of this PaymentRequest.  # noqa: E501


        :return: The channel of this PaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this PaymentRequest.


        :param channel: The channel of this PaymentRequest.  # noqa: E501
        :type: str
        """

        self._channel = channel

    @property
    def terminal(self):
        """Gets the terminal of this PaymentRequest.  # noqa: E501

        The terminal number assigned by the gateway.  # noqa: E501

        :return: The terminal of this PaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this PaymentRequest.

        The terminal number assigned by the gateway.  # noqa: E501

        :param terminal: The terminal of this PaymentRequest.  # noqa: E501
        :type: str
        """
        if terminal is None:
            raise ValueError("Invalid value for `terminal`, must not be `None`")  # noqa: E501

        self._terminal = terminal

    @property
    def operator(self):
        """Gets the operator of this PaymentRequest.  # noqa: E501

        The operator who initiated the transaction. If not sent in the request, this field will be automatically populated with the API Key alias.  # noqa: E501

        :return: The operator of this PaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this PaymentRequest.

        The operator who initiated the transaction. If not sent in the request, this field will be automatically populated with the API Key alias.  # noqa: E501

        :param operator: The operator of this PaymentRequest.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def order(self):
        """Gets the order of this PaymentRequest.  # noqa: E501


        :return: The order of this PaymentRequest.  # noqa: E501
        :rtype: Order
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this PaymentRequest.


        :param order: The order of this PaymentRequest.  # noqa: E501
        :type: Order
        """
        if order is None:
            raise ValueError("Invalid value for `order`, must not be `None`")  # noqa: E501

        self._order = order

    @property
    def customer(self):
        """Gets the customer of this PaymentRequest.  # noqa: E501


        :return: The customer of this PaymentRequest.  # noqa: E501
        :rtype: Customer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this PaymentRequest.


        :param customer: The customer of this PaymentRequest.  # noqa: E501
        :type: Customer
        """

        self._customer = customer

    @property
    def customer_account(self):
        """Gets the customer_account of this PaymentRequest.  # noqa: E501


        :return: The customer_account of this PaymentRequest.  # noqa: E501
        :rtype: Payload
        """
        return self._customer_account

    @customer_account.setter
    def customer_account(self, customer_account):
        """Sets the customer_account of this PaymentRequest.


        :param customer_account: The customer_account of this PaymentRequest.  # noqa: E501
        :type: Payload
        """

        self._customer_account = customer_account

    @property
    def credential_on_file(self):
        """Gets the credential_on_file of this PaymentRequest.  # noqa: E501


        :return: The credential_on_file of this PaymentRequest.  # noqa: E501
        :rtype: CredentialOnFile
        """
        return self._credential_on_file

    @credential_on_file.setter
    def credential_on_file(self, credential_on_file):
        """Sets the credential_on_file of this PaymentRequest.


        :param credential_on_file: The credential_on_file of this PaymentRequest.  # noqa: E501
        :type: CredentialOnFile
        """

        self._credential_on_file = credential_on_file

    @property
    def ip_address(self):
        """Gets the ip_address of this PaymentRequest.  # noqa: E501


        :return: The ip_address of this PaymentRequest.  # noqa: E501
        :rtype: IpAddress
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this PaymentRequest.


        :param ip_address: The ip_address of this PaymentRequest.  # noqa: E501
        :type: IpAddress
        """

        self._ip_address = ip_address

    @property
    def auto_capture(self):
        """Gets the auto_capture of this PaymentRequest.  # noqa: E501

        It indicates whether the amount of the transaction should be automatically and fully captured.  - `true` : the gateway will automatically set the transaction to `READY` making it eligible for the next settlement run. - `false`: a pre-authorization will be performed if your account has the \"Allow Pre-Auth\" feature enabled. Otherwise, a regular transaction will be created with `PENDING` status. Either way, an additional call to the [Capture a Payment](#operation/capturePayment) operation is required to capture the final amount and flag the transaction as ready for the next settlement run.  # noqa: E501

        :return: The auto_capture of this PaymentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_capture

    @auto_capture.setter
    def auto_capture(self, auto_capture):
        """Sets the auto_capture of this PaymentRequest.

        It indicates whether the amount of the transaction should be automatically and fully captured.  - `true` : the gateway will automatically set the transaction to `READY` making it eligible for the next settlement run. - `false`: a pre-authorization will be performed if your account has the \"Allow Pre-Auth\" feature enabled. Otherwise, a regular transaction will be created with `PENDING` status. Either way, an additional call to the [Capture a Payment](#operation/capturePayment) operation is required to capture the final amount and flag the transaction as ready for the next settlement run.  # noqa: E501

        :param auto_capture: The auto_capture of this PaymentRequest.  # noqa: E501
        :type: bool
        """

        self._auto_capture = auto_capture

    @property
    def process_as_sale(self):
        """Gets the process_as_sale of this PaymentRequest.  # noqa: E501

        Indicates whether the transaction should be processed as a Sale. A Sale transaction is characterized by its `COMPLETE` status due to the fact that authorization and settlement operations are performed at the same time. This means that this kind of transaction is not subject to changes or late adjustments even while sitting in the open batch.  **Note:** The `autoCapture` indicator must be set to TRUE to process a Sale.  # noqa: E501

        :return: The process_as_sale of this PaymentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._process_as_sale

    @process_as_sale.setter
    def process_as_sale(self, process_as_sale):
        """Sets the process_as_sale of this PaymentRequest.

        Indicates whether the transaction should be processed as a Sale. A Sale transaction is characterized by its `COMPLETE` status due to the fact that authorization and settlement operations are performed at the same time. This means that this kind of transaction is not subject to changes or late adjustments even while sitting in the open batch.  **Note:** The `autoCapture` indicator must be set to TRUE to process a Sale.  # noqa: E501

        :param process_as_sale: The process_as_sale of this PaymentRequest.  # noqa: E501
        :type: bool
        """

        self._process_as_sale = process_as_sale

    @property
    def offline_processing(self):
        """Gets the offline_processing of this PaymentRequest.  # noqa: E501


        :return: The offline_processing of this PaymentRequest.  # noqa: E501
        :rtype: OfflineProcessing
        """
        return self._offline_processing

    @offline_processing.setter
    def offline_processing(self, offline_processing):
        """Sets the offline_processing of this PaymentRequest.


        :param offline_processing: The offline_processing of this PaymentRequest.  # noqa: E501
        :type: OfflineProcessing
        """

        self._offline_processing = offline_processing

    @property
    def additional_data_fields(self):
        """Gets the additional_data_fields of this PaymentRequest.  # noqa: E501

        List of custom fields which are used to add extra information to transactions. Their values are going to be stored and used for the requests sent to the terminal's receipt and validation webhooks.<br />For more information, visit the section [Special Fields and Parameters](https://docs.worldnettps.com/doku.php?id=developer:api_specification:special_fields_and_parameters) of our knowledge base.  # noqa: E501

        :return: The additional_data_fields of this PaymentRequest.  # noqa: E501
        :rtype: list[CustomField]
        """
        return self._additional_data_fields

    @additional_data_fields.setter
    def additional_data_fields(self, additional_data_fields):
        """Sets the additional_data_fields of this PaymentRequest.

        List of custom fields which are used to add extra information to transactions. Their values are going to be stored and used for the requests sent to the terminal's receipt and validation webhooks.<br />For more information, visit the section [Special Fields and Parameters](https://docs.worldnettps.com/doku.php?id=developer:api_specification:special_fields_and_parameters) of our knowledge base.  # noqa: E501

        :param additional_data_fields: The additional_data_fields of this PaymentRequest.  # noqa: E501
        :type: list[CustomField]
        """

        self._additional_data_fields = additional_data_fields

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PaymentRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PaymentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
