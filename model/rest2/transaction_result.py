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


class TransactionResult(object):
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
        'type': 'str',
        'status': 'str',
        'approval_code': 'str',
        'date_time': 'datetime',
        'currency': 'str',
        'authorized_amount': 'float',
        'result_code': 'str',
        'result_message': 'str',
        'processor_result_code': 'str',
        'stored_payment_credentials': 'SecureCredentials'
    }

    attribute_map = {
        'type': 'type',
        'status': 'status',
        'approval_code': 'approvalCode',
        'date_time': 'dateTime',
        'currency': 'currency',
        'authorized_amount': 'authorizedAmount',
        'result_code': 'resultCode',
        'result_message': 'resultMessage',
        'processor_result_code': 'processorResultCode',
        'stored_payment_credentials': 'storedPaymentCredentials'
    }

    def __init__(self, type=None, status=None, approval_code=None, date_time=None, currency=None, authorized_amount=None, result_code=None, result_message=None, processor_result_code=None, stored_payment_credentials=None):  # noqa: E501
        """TransactionResult - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._status = None
        self._approval_code = None
        self._date_time = None
        self._currency = None
        self._authorized_amount = None
        self._result_code = None
        self._result_message = None
        self._processor_result_code = None
        self._stored_payment_credentials = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if approval_code is not None:
            self.approval_code = approval_code
        if date_time is not None:
            self.date_time = date_time
        if currency is not None:
            self.currency = currency
        if authorized_amount is not None:
            self.authorized_amount = authorized_amount
        if result_code is not None:
            self.result_code = result_code
        if result_message is not None:
            self.result_message = result_message
        if processor_result_code is not None:
            self.processor_result_code = processor_result_code
        if stored_payment_credentials is not None:
            self.stored_payment_credentials = stored_payment_credentials

    @property
    def type(self):
        """Gets the type of this TransactionResult.  # noqa: E501

        The type of the generated transaction.  # noqa: E501

        :return: The type of this TransactionResult.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TransactionResult.

        The type of the generated transaction.  # noqa: E501

        :param type: The type of this TransactionResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["SALE", "PREAUTH", "COMPLETION", "REFUND", "OFFLINE_DECLINE", "WITHDRAWAL"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def status(self):
        """Gets the status of this TransactionResult.  # noqa: E501

        The current status of the generated transaction.  # noqa: E501

        :return: The status of this TransactionResult.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TransactionResult.

        The current status of the generated transaction.  # noqa: E501

        :param status: The status of this TransactionResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["READY", "PENDING", "VOID", "DECLINED", "COMPLETE", "REFERRAL", "PICKUP", "REVERSAL", "SENT", "ADMIN", "EXPIRED", "ACCEPTED", "REVIEW", "OTHER"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def approval_code(self):
        """Gets the approval_code of this TransactionResult.  # noqa: E501

        The authorization code assigned by the payment processor for approved transactions.  # noqa: E501

        :return: The approval_code of this TransactionResult.  # noqa: E501
        :rtype: str
        """
        return self._approval_code

    @approval_code.setter
    def approval_code(self, approval_code):
        """Sets the approval_code of this TransactionResult.

        The authorization code assigned by the payment processor for approved transactions.  # noqa: E501

        :param approval_code: The approval_code of this TransactionResult.  # noqa: E501
        :type: str
        """

        self._approval_code = approval_code

    @property
    def date_time(self):
        """Gets the date_time of this TransactionResult.  # noqa: E501

        The processing date and time of the transaction represented as per [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard.  # noqa: E501

        :return: The date_time of this TransactionResult.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this TransactionResult.

        The processing date and time of the transaction represented as per [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard.  # noqa: E501

        :param date_time: The date_time of this TransactionResult.  # noqa: E501
        :type: datetime
        """

        self._date_time = date_time

    @property
    def currency(self):
        """Gets the currency of this TransactionResult.  # noqa: E501

        The currency of the transaction. A 3-letter code as per the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217#Active_codes) standard.  # noqa: E501

        :return: The currency of this TransactionResult.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this TransactionResult.

        The currency of the transaction. A 3-letter code as per the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217#Active_codes) standard.  # noqa: E501

        :param currency: The currency of this TransactionResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BOV", "BRL", "BSD", "BTN", "BWP", "BYR", "BZD", "CAD", "CDF", "CHE", "CHF", "CHW", "CLF", "CLP", "CNY", "COP", "COU", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MRU", "MUR", "MVR", "MWK", "MXN", "MXV", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STD", "STN", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "USN", "USS", "UYI", "UYU", "UZS", "VEF", "VES", "VND", "VUV", "WST", "XAF", "XCD", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWL"]  # noqa: E501
        if currency not in allowed_values:
            raise ValueError(
                "Invalid value for `currency` ({0}), must be one of {1}"  # noqa: E501
                .format(currency, allowed_values)
            )

        self._currency = currency

    @property
    def authorized_amount(self):
        """Gets the authorized_amount of this TransactionResult.  # noqa: E501

        The amount authorized by the payment processor.  **Note:** For partial authorizations, this amount will be lower than the actual amount sent in the request.<br />**Note:** This amount will be negative for refund transactions to represent the return of funds back to the customer's account.  # noqa: E501

        :return: The authorized_amount of this TransactionResult.  # noqa: E501
        :rtype: float
        """
        return self._authorized_amount

    @authorized_amount.setter
    def authorized_amount(self, authorized_amount):
        """Sets the authorized_amount of this TransactionResult.

        The amount authorized by the payment processor.  **Note:** For partial authorizations, this amount will be lower than the actual amount sent in the request.<br />**Note:** This amount will be negative for refund transactions to represent the return of funds back to the customer's account.  # noqa: E501

        :param authorized_amount: The authorized_amount of this TransactionResult.  # noqa: E501
        :type: float
        """

        self._authorized_amount = authorized_amount

    @property
    def result_code(self):
        """Gets the result_code of this TransactionResult.  # noqa: E501

        Our platform maps result codes sent by different payment processors into a smaller set of codes as shown below. The original result code may be available in the `processorResultCode` field.  - **A**: Approved / Authorized. - **D**: Declined / Not Authorized. - **E**: Accepted for later processing, but result currently unknown. - **P**: Only a portion of the original amount requested was authorized. - **R**: Issuer has declined the transaction and indicated that the customer should contact their bank. - **C**: Issuer has declined the transaction and requested that the card be retained as it may have been reported as lost or stolen.  # noqa: E501

        :return: The result_code of this TransactionResult.  # noqa: E501
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """Sets the result_code of this TransactionResult.

        Our platform maps result codes sent by different payment processors into a smaller set of codes as shown below. The original result code may be available in the `processorResultCode` field.  - **A**: Approved / Authorized. - **D**: Declined / Not Authorized. - **E**: Accepted for later processing, but result currently unknown. - **P**: Only a portion of the original amount requested was authorized. - **R**: Issuer has declined the transaction and indicated that the customer should contact their bank. - **C**: Issuer has declined the transaction and requested that the card be retained as it may have been reported as lost or stolen.  # noqa: E501

        :param result_code: The result_code of this TransactionResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["A", "D", "E", "P", "R", "C"]  # noqa: E501
        if result_code not in allowed_values:
            raise ValueError(
                "Invalid value for `result_code` ({0}), must be one of {1}"  # noqa: E501
                .format(result_code, allowed_values)
            )

        self._result_code = result_code

    @property
    def result_message(self):
        """Gets the result_message of this TransactionResult.  # noqa: E501

        A brief description sent by the processor about the transaction result.<br />Clients must use this description in order to understand the cause of rejections and declines.  # noqa: E501

        :return: The result_message of this TransactionResult.  # noqa: E501
        :rtype: str
        """
        return self._result_message

    @result_message.setter
    def result_message(self, result_message):
        """Sets the result_message of this TransactionResult.

        A brief description sent by the processor about the transaction result.<br />Clients must use this description in order to understand the cause of rejections and declines.  # noqa: E501

        :param result_message: The result_message of this TransactionResult.  # noqa: E501
        :type: str
        """

        self._result_message = result_message

    @property
    def processor_result_code(self):
        """Gets the processor_result_code of this TransactionResult.  # noqa: E501

        The original result code sent by the payment processor.  # noqa: E501

        :return: The processor_result_code of this TransactionResult.  # noqa: E501
        :rtype: str
        """
        return self._processor_result_code

    @processor_result_code.setter
    def processor_result_code(self, processor_result_code):
        """Sets the processor_result_code of this TransactionResult.

        The original result code sent by the payment processor.  # noqa: E501

        :param processor_result_code: The processor_result_code of this TransactionResult.  # noqa: E501
        :type: str
        """

        self._processor_result_code = processor_result_code

    @property
    def stored_payment_credentials(self):
        """Gets the stored_payment_credentials of this TransactionResult.  # noqa: E501


        :return: The stored_payment_credentials of this TransactionResult.  # noqa: E501
        :rtype: SecureCredentials
        """
        return self._stored_payment_credentials

    @stored_payment_credentials.setter
    def stored_payment_credentials(self, stored_payment_credentials):
        """Sets the stored_payment_credentials of this TransactionResult.


        :param stored_payment_credentials: The stored_payment_credentials of this TransactionResult.  # noqa: E501
        :type: SecureCredentials
        """

        self._stored_payment_credentials = stored_payment_credentials

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
        if issubclass(TransactionResult, dict):
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
        if not isinstance(other, TransactionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
