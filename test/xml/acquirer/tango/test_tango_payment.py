import random

from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import Currency, INTERAC_CARDS, TransactionType
from data.rest_requests import rest_emv_tlv_sale, rest_track2_sale
from data.xml_requests import payment, payment_avs
from model.gateway import PAYMENTRESPONSE
from model.rest import transactionResponse
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
TERM_ID = '21004'
USD_TERM_ID = '21010'
MC_TERM_ID = '21011'
VISA_EDCC = '4485910301709438'  # GPB > USD


def test_tango_moto_cad_approved_payment():
    p = payment()
    p.CURRENCY = Currency.CAD.name
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_tango_mc_moto_payment():
    p = payment()
    p.CURRENCY = Currency.CAD.name
    response = wn.xml(terminal_id=MC_TERM_ID).payment(request=p, is_multicurrency=True)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_tango_mc_exchage_rate_payment():
    p = payment()
    p.CURRENCY = Currency.GBP.name
    response = wn.xml(terminal_id=MC_TERM_ID).payment(request=p, is_multicurrency=True)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    # check logs for conversion: {..."TxDtls":{"CcyCd":"GBP","TtlAmt":"6.83","UattnddLvlCtgy":"LVL6","MrchntAmts"
    # :{"CcyCd":"CAD","TtlAmt":"11.91","XchgRate":"1.7433750"}


def test_tango_moto_usd_approved_payment():
    p = payment()
    p.CARDNUMBER = '4111111111111111'
    p.CURRENCY = Currency.USD.name
    response = wn.xml(terminal_id=USD_TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_tango_interac_card_payment():
    p = payment()
    p.CARDNUMBER = random.choice(INTERAC_CARDS)
    p.CARDTYPE = 'VISA DEBIT'
    p.CURRENCY = Currency.CAD.name
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_tango_unsupported_currency():
    wn.boarding().update_terminal_currency(TERM_ID, Currency.USD)
    p = payment()
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))
    wn.boarding().update_terminal_currency(TERM_ID, Currency.CAD)


def test_tango_avs_payment():
    # t = wn.boarding().get_terminal(TERM_ID)
    # t.securityFraud.enableAvs = True
    # t.securityFraud.avsSentAction = 'DISPLAY'
    # wn.boarding().update_terminal(t)

    p = payment_avs()
    p.CURRENCY = Currency.CAD.name
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    # t.securityFraud.enableAvs = False
    # wn.boarding().update_terminal(t)


def test_tango_contactless_icc_sale():
    p = rest_emv_tlv_sale(amount=10.08, currency=Currency.CAD)
    p.cardEntryMode = 'CONTACTLESS_ICC'
    p.paymentMethod.emvTlv.tlvString = 'DF7903312e305F20009F42020840DF7807FFFF65432100009f0607A0000000041010C00AFFFF654321000040094EC408541333FFFFFF4111C28201A845D6B5B689E9A286D39082408918F5868CAD429B21D8BD5374CF6B6692182E69E90A2BBB4EA694CDF73904DFD30050560539DACEF2883C23920E173147A8DB3972C051EF1FCC95D794D2094639D7AE39955ABCB439FC885A1BEC347B5684D96683AD90AD8317B1151478CC18B267E9137FE9DC6AE9408BEAB8005C2FF983034B8D50CECE8F857936E3973DDDEE7E85440571AE8DC3FB3D8D8BC9A0ADBEF886DEFF8607E96F1E6526CF7E1402AC1503CEFB43B9B64A703B234D2A88369E428045D15EFC524516A38715CC2E2171E28C68B1F20AA5ADC0EA353847A1C940CE6E103A6293DDE7D89B7F486A27574FBF20F10644058663439BDD5DB50E505AF0C3809E801A793493BDBA05CE40882CC052832A62529FE025DBE4A8E1222D7609FF062C4AB437E82BF04B56C049E96C5AC55290F3D3D01F163E6884F9F4FD9E01A080B810D03F5679B225DA8CCC74346B97A48AE4D91B6BA351704C43C06BA9641756B9DD12D0FDEF63E94C047D4C973E435648DB81BF350F24EBD0EFB5F46065C0EF0423C858D924263F6BB4C51D4A94BA97385EFC15929EF11FB3956F104BD889173741C4D78DCA7B7DC70AFFFF65432100006009EBC81829A0C7A843A118FA408A7B33ADDBFFA21C002192ECF62E504F07A00000000410105F24032212315F2A02084082021980950500000080009A031908299B02E0009C01009F02060000000010009F03060000000000009F0607A00000000410109F10120110A04003220000000000000000000000FF9F120A4D6173746572436172649F1A0208409F1C0831313232333334349F21031304249F26086B7B3812EC4BBA689F2701809F33036008C89F34031F03029F36020A509F37044ADF33CE9F390107DF826E0F575043323534363235303030343033DF080A0004654321000080094CCD08A56A1E2327020570'
    p.paymentMethod.emvTlv.ksn = 'FFFF654321000040094E'
    response = wn.rest(TERM_ID).sale(request=p)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))


def test_tango_contactless_msr_sale():
    p = rest_track2_sale(amount=5)
    response = wn.rest(TERM_ID).sale(request=p, currency=Currency.CAD)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))


def test_tango_3ds_payment():
    p = payment(cardtype='visa')
    p.TRANSACTIONTYPE = TransactionType.THREE_DS
    p.CURRENCY = Currency.CAD.name
    p.MPIREF = 'b51adf32aa5e81ab2528'
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    db_txn = wn.db(terminal_number=TERM_ID).get_transaction(uniqueref=response.UNIQUEREF)
    assert_that(db_txn.commercetype, equal_to(str(TransactionType.THREE_DS)))
