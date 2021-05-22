import pytest
from faker import Factory
from hamcrest import assert_that, instance_of

from constants import PaynomixCard
from data.xml_requests import securecard_registration, payment_securecard
from model.gateway import SECURECARDREGISTRATIONRESPONSE, PAYMENTRESPONSE
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.wn
TERM_ID = '22015'


@pytest.mark.parametrize('card', PaynomixCard)
def test_paynomix_securecard_registration(card):
    sc = securecard_registration()
    sc.CARDNUMBER = card.cardnumber  # no cvv, not mandatory for paynomix
    sc.MERCHANTREF = card.merchant_ref
    response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))


def test_securecard_payment():
    # TODO check with enabled sc validation
    sc = securecard_registration()
    sc.CARDNUMBER = PaynomixCard.rand().cardnumber  # no cvv, not mandatory for paynomix
    secure_card = wn.xml(TERM_ID).secure_card_registration()
    assert_that(secure_card, instance_of(SECURECARDREGISTRATIONRESPONSE))

    response = wn.xml(TERM_ID).payment(payment_securecard(cardreference=secure_card.CARDREFERENCE))
    assert_that(response, instance_of(PAYMENTRESPONSE))

    wn.xml(TERM_ID).secure_card_removal(secure_card.MERCHANTREF, secure_card.CARDREFERENCE)
