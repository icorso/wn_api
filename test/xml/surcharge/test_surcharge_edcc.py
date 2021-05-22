from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import Currency
from data.xml_requests import payment_edcc
from model.gateway import PAYMENTRESPONSE
from utils import random_amount, SurchargeAmount, random_surcharge_percent
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().local.go
wn_boarding = WNClient().local.go.boarding()
wn_db = WNClient().db()
TERM_ID = '21001'
VISA_EDCC = '4485910301709438'  # GPB > USD
CURRENCY = Currency.USD
SUR_PERCENT = random_surcharge_percent()
AMOUNT = random_amount(currency=CURRENCY)


def test_surcharge_edcc_payment():
    surcharge = SurchargeAmount(AMOUNT, SUR_PERCENT)
    wn_boarding.update_terminal_surcharge(terminal_number=TERM_ID, allow_surcharge=True, surcharge_percent=SUR_PERCENT)

    response = wn.xml(TERM_ID).get_card_currency_rate(VISA_EDCC[:6], surcharge.total_amount)

    p = payment_edcc(amount=surcharge.total_amount,
                     cardnumber=VISA_EDCC,
                     conversion_rate=response.CONVERSIONRATE,
                     card_currency=Currency.GBP,
                     terminal_currency=Currency.USD)
    payment_response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))

    db_surcharge = wn.db(terminal_number=TERM_ID).get_transaction_surcharge(uniqueref=payment_response.UNIQUEREF)
    assert_that(db_surcharge.amount, equal_to(surcharge.surcharge))
