from hamcrest import assert_that, equal_to, instance_of

from constants import Currency
from data.rest_requests import rest_sale, rest_emv_tlv_sale, rest_applepay_sale, rest_track2_sale, \
    rest_securecard_sale, rest_track2contactless
from model.rest import terminalType, serviceError, transactionResponse, paymentMethod, posDevice, keyedAsTrackData, \
    keyedEncrypted
from wnclient import WNClient

wn = WNClient().vagrant.go
wn_boarding = WNClient().vagrant.go.boarding()
TERM_ID = '21001'


def test_rest_keyed_card_sale():
    wn_boarding.with_terminal(TERM_ID).update_terminal_cards(TERM_ID, silence=True)
    r = rest_sale()
    r.paymentMethod.keyedCard.cardNumber = '6385087787065456'
    r.paymentMethod.keyedCard.cardType = ''
    response = wn.rest(TERM_ID).sale(r)
    assert_that(response, instance_of(serviceError))
    assert_that(response.message, equal_to('Invalid card type'))


def test_rest_keyed_encrypted_card_sale():
    wn_boarding.with_terminal(TERM_ID).update_terminal_cards(TERM_ID, silence=True)
    r = rest_sale()
    r.device = posDevice(serialNumber='WPC254625000403', type_='WISEPAD')
    r.account.terminalType = 'CHP'
    # encrypted value cardnumber 6385087787065456, BDK index 2
    pm = paymentMethod(
        keyedEncrypted=keyedEncrypted(
            expiryDate='2110',
            panEncrypted='1B27B0AAC2DD7643',
            panMasked='638508XXXXXX5456',
            ksn='88888813710009600123'
    ))
    r.paymentMethod = pm
    response = wn.rest(TERM_ID).sale(r)
    assert_that(response, instance_of(serviceError))
    assert_that(response.message, equal_to('Invalid card type'))


def test_rest_keyed_as_track2_sale():
    wn_boarding.with_terminal(TERM_ID).update_terminal_cards(TERM_ID, silence=True)
    r = rest_sale()
    r.device = posDevice(serialNumber='WPC254625000403', type_='INGENICO_ICT220')
    r.account.terminalType = 'CHP'
    # encrypted value 6385087787065456=2012123 , / BDK index 2
    #                 M6A959E03745D7B6=D4F1A264E793B348D
    pm = paymentMethod(
        keyedAsTrack2=keyedAsTrackData(
            encryptedData='M6A959E03745D7B6=D4F1A264E793B348D',
            ksn='88888813710009600123',
            firstDigitOfPan='6',
            serial='262677000000016'
    ))
    r.paymentMethod = pm
    response = wn.rest(TERM_ID).sale(r)
    assert_that(response, instance_of(serviceError))
    assert_that(response.message, equal_to('Invalid card type'))


def test_rest_track2_sale():
    r = rest_track2_sale()
    # raw track data ;6385087787065456=25121011796251900000?
    r.paymentMethod.track2.cardType = ''
    r.paymentMethod.track2.encryptedData = 'B3F237FDC311B6241A4A73A243080C5FA2196F4B62DE2C0F'
    response = wn.rest(TERM_ID).sale(r)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.receiptFields.cardType, equal_to('Visa Credit'))


def test_rest_track2contactless_sale():
    # raw track data ;6385087787065456=25121011796251900000?
    r = rest_sale()
    r.paymentMethod = paymentMethod(track2Contactless=rest_track2contactless())
    r.paymentMethod.track2Contactless.cardType = ''
    r.paymentMethod.track2Contactless.ksn = '88888813710009600123'
    r.paymentMethod.track2Contactless.encryptedData = 'B3F237FDC311B6241A4A73A243080C5FA2196F4B62DE2C0F'
    r.device = posDevice(serialNumber='WPC254625000403', type_='WISEPAD')
    response = wn.rest(TERM_ID).sale(r)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.receiptFields.cardType, equal_to('Visa Credit'))


def test_rest_emv_tlv_sale():
    wn_boarding.with_terminal(TERM_ID).update_terminal_cards(TERM_ID, ['visa'], silence=True)

    p = rest_emv_tlv_sale(currency=Currency.USD)
    p.paymentMethod.emvTlv.cardType = ''
    p.paymentMethod.emvTlv.tlvString = '4F07A00000000310108A025a31950508800080009B02E800C00A03000000000000000001C282019849FFF16BC9C5520D3C5C133C03D52715F2602F5D3A8B4AF9B0562C24FD717077558A107978598746D3B14945861C33F35BAB4738D7DFCFAE28E5830373ED073CBC4DC5F9D5AA3D3D9917D62810676EA224A03D417AA1B693007BA3F1C01E2E8AF650FDF4DE557EBF0CCA7D28855CD4FDC6ED129A791F788CF72096E67EB1DFE0125AA339C8FC036FDA4D3083B6DA0EDEF5916CF943BF43BD8CD49402B8151F58D6623A50F26F083898708C1A48598EA395E8A687B93B5CCEF7A66DFE1E7B0492F4C1281325C23AF4C668EA30F1FE4A8C3E6EEB5348C2EDE94106D439ED65A853669D2224231C406D4EE9F72053D59522D7EC485C950CB7EF3A14F050EE2CC5AE19A20EB043DE3109E012AAD45FD4EFA067E6D65858DD81EEAD30951CB6A53DE09131E67E757C35319D9A68B8B14395214ADCE1BFEE401121965903A12CDED4430C2BA3497AA974B398C7D947650CBBFC54D098A1B19EF3887C7245DCF571A7404B998452B4734717119A055AC2B12C47F04698827F948EA61D066A6E0DDF8FB1BF45AFAC833DF855E060ED9B9A51E39777296281CE398B49C408541333ffffff0681C70A88828888888888e00174C81860d743c93014856dbed7bd9815914b4bc32f47e76c53b006CD082a2a18971dcafc43CE0A88858888888888e0026f5F20084A6F686E20446F655F24031912319F02060000001010009F03060000000000009F120A4d6173746572436172649F1C04000100019F2608D83A8CE1F787D51D9F2701809F42020840DF780703000000000000DF791000003300b135ff832636454e1f000830'
    p.paymentMethod.emvTlv.ksn = '03000000000000000001'
    response = wn.rest(TERM_ID).sale(request=p)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.receiptFields.cardType, equal_to('Visa Credit'))


def test_securecard_sale():
    payment = rest_securecard_sale('2967539933907556')
    response = wn.go.rest('21001').sale(payment)
    assert_that(response, instance_of(transactionResponse))


def test_applepay_rest_sale():
    payment = rest_applepay_sale()
    payment.account.terminalType = terminalType.INTERNET
    payment.amount.amount = 66.00
    wn.go.rest('21003').sale(payment)
