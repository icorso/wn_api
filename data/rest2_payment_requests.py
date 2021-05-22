from faker import Factory

from constants import Currency, PosDevice
from data.rest2_common import rest2_card_details, rest2_customer, rest2_keyed_payload
from model.rest2 import Order, RefundPaymentRequest, KeyedPayload, MotoPaymentRequest, \
    OfflineProcessing, CapturePaymentRequest, PosPaymentRequest, EmvPayload, EncryptionCapableDevice, MagStripePayload, \
    ReversePaymentRequest, SecureCredentialsPayload, RefundRequest, MagStripeDataFormat, EncryptedMagStripeDataFormat, \
    UpdatePaymentRequest, CustomerUpdatableData
from utils import today, random_amount

fake = Factory.create()
today = today(format='%Y-%m-%dT%H:%M:%S')


def rest2_order(amount_=None, currency: Currency = Currency.USD):
    amount = amount_ if amount_ is not None else random_amount(currency=currency, digits=2)

    return Order(
        total_amount=amount,
        currency=currency.name,
        order_id=f'REST2_{str(fake.random_number(7, False))}',
        description=fake.text(10)
    )


def rest2_payment_moto(currency: Currency = Currency.USD, cardtype=None, cvv=None) -> MotoPaymentRequest:
    payment_request = MotoPaymentRequest(
        channel='MOTO',
        operator=fake.name(),
        order=rest2_order(currency=currency),
        customer_account=rest2_keyed_payload(),
        customer=rest2_customer()
    )
    return payment_request


def rest2_credentials_payment(credentials_number, currency: Currency = Currency.USD) -> MotoPaymentRequest:
    payment_request = MotoPaymentRequest(
        channel='WEB',
        operator=fake.name(),
        order=rest2_order(currency=currency),
        customer_account=SecureCredentialsPayload(
            payload_type='SECURE_CREDENTIALS',
            account_type='CHECKING',
            credentials_number=credentials_number
        ),
        customer=rest2_customer()
    )
    return payment_request


def rest2_payment_refund(amount, reason=None, operator=None) -> RefundPaymentRequest:
    return RefundPaymentRequest(
        operator=operator if operator else fake.name(),
        refund_amount=amount,
        refund_reason=reason if reason else fake.text(15),
    )


def rest2_payment_reverse(amount, reason=None, operator=None, customer_account=None) -> ReversePaymentRequest:
    return ReversePaymentRequest(
        operator=operator,
        reversal_amount=amount,
        reversal_reason=reason if reason else fake.text(15),
        customer_account=customer_account
    )


def rest2_payment_update() -> UpdatePaymentRequest:
    return UpdatePaymentRequest(
        operator=fake.name(),
        total_amount=random_amount(),
        customer=CustomerUpdatableData(
            phone=fake.random_number(),
            email=fake.free_email()
        )
    )


def rest2_payment_offline(operation='OFFLINE_APPROVAL', approval_code='A', cardtype=None, cvv=None) -> MotoPaymentRequest:
    payment_request = rest2_payment_moto(cardtype=cardtype, cvv=cvv)
    payment_request.offline_processing = OfflineProcessing(
            operation=operation,
            approval_code=approval_code
    )
    return payment_request


def rest2_capture_payment(capture_amount=None, operator=None) -> CapturePaymentRequest:
    return CapturePaymentRequest(
        operator=operator if operator else fake.name(),
        capture_amount=capture_amount
    )


def rest2_payment_emv(tlv_string, ksn, device_type=PosDevice.WISEPAD, currency=Currency.USD) -> PosPaymentRequest:
    payment_request = PosPaymentRequest(
        channel='POS',
        operator=fake.name(),
        order=rest2_order(currency=currency),
        customer_account=EmvPayload(
            payload_type='EMV',
            device=EncryptionCapableDevice(
                type=device_type.name,
                data_ksn=ksn
            ),
            tlv=tlv_string
        ),
        customer=rest2_customer()
    )
    return payment_request


def rest2_payment_msr_encrypted(encrypted_data, ksn, additional_tlv_data=None, device_type=PosDevice.WISEPAD,
                                currency=Currency.USD) -> PosPaymentRequest:
    payment_request = PosPaymentRequest(
        channel='POS',
        operator=fake.name(),
        order=rest2_order(currency=currency),
        customer_account=MagStripePayload(
            payload_type='MAG_STRIPE',
            card_details=EncryptedMagStripeDataFormat(
                data_format='ENCRYPTED',
                device=EncryptionCapableDevice(
                    serial_number=fake.random_number(8),
                    category='UNATTENDED',
                    type=device_type.name,
                    data_ksn=ksn
                ),
                encrypted_data=encrypted_data
            ),
            additional_tlv_data=additional_tlv_data
        ),
        customer=rest2_customer()
    )
    return payment_request


def rest2_unreferenced_refund_keyed(amount=None, reason=None, currency: Currency = Currency.USD, cardtype=None, cvv=None) -> RefundRequest:
    refund_request = RefundRequest(
        channel='MOTO',
        operator=fake.name(),
        refund_amount=amount if amount else random_amount(currency=currency),
        refund_reason=reason if reason else fake.text(20),
        order_id='MAPI_' + str(fake.random_number(fix_len=True, digits=5)),
        currency=currency.name,
        customer_account=KeyedPayload(
            cardholder_name=fake.name(),
            payload_type='KEYED',
            account_type='CHECKING',
            card_details=rest2_card_details(cardtype, cvv)
        ),
        customer=rest2_customer()
    )
    return refund_request

