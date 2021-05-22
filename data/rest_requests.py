from datetime import datetime
from decimal import Decimal

from faker import Factory

from constants import Currency, FiServCard, PosDevice, EmvTlv
from model.rest import sale, account, commerceType, customer, terminalType, amount, keyedCard, paymentMethod, reversal, \
    refund, refundReferenced, refundMethod, androidWallet, emvtlv, taxesType, tax, tipType, tip, posDevice, trackData, \
    appleWallet, refundUnreferenced, cardDetails, secureCardMethod, trackDataContactless, voucher, tipAdjustment, \
    transactionUpdate, balanceInquiry, dukptPinDetails, pinDetails, secureCard, keyedSecureCard, cardEntryMode, \
    tokenMethod, keyedAsTrackData, keyedEncrypted, emv
from utils import random_text
from utils import today, random_amount, random_card

fake = Factory.create()
today = today(format='%Y-%m-%dT%H:%M:%S')


def rest_account(terminal_id=None, device_type=PosDevice.WISEPAD.device_name):
    return account(
        deviceId=device_type,
        operator=fake.name(),
        terminalType=terminalType.INTERNET,
        terminalId=terminal_id
    )


def rest_card_details(cardtype=None):
    creditcard = random_card(cardtype=cardtype) if cardtype else random_card()
    cd = cardDetails(
        cardType=creditcard.cardtype,
        cardNumber=creditcard.cardnumber,
        expiryDate=creditcard.cardexpiry
    )
    return cd


def rest_customer():
    return customer(
        city=fake.city(),
        country=fake.country(),
        eMail=fake.free_email(),
        ipAddress=fake.ipv4(),
        mobileNumber=fake.msisdn(),
        region=fake.state(),
        # signature='00010B000P001E0424090000'
    )


def rest_amount(amount_=None, currency='USD'):
    return amount(
        amount_member=Decimal(amount_) if amount_ else fake.pydecimal(1, Currency[currency].minorunits, True),
        currency=currency
    )


def rest_pos_device(device_type=PosDevice.WISEPAD.device_name):
    return posDevice(serialNumber=random_text(5) + device_type, type_=device_type)


def rest_keyed_card(cardtype='visa', cvv='999'):
    card = random_card(cardtype=cardtype)
    return keyedCard(
        cardHolderName=card.cardholder,
        cardNumber=card.cardnumber,
        cardType=cardtype,
        expiryDate=card.cardexpiry,
        cvv=cvv
    )


def rest_tip_adjustment(amount, currency: Currency, tip_type: tipType, percentage=None):
    ta = tipAdjustment(
        amount_member=amount,
        tipType=tip_type,
        currency=currency.name,
        percentage=percentage
    )
    return ta


def rest_transaction_tip_adjustment(uniqueref, tip_type: tipType, currency: Currency, amount=None, percentage=None):
    return transactionUpdate(
        uniqueRef=uniqueref,
        dateTime=datetime.now().replace(microsecond=0),
        deviceType='WALKER',
        account=rest_account(),
        tipAdjustment=tipAdjustment(
            amount_member=amount,
            currency=currency.name,
            percentage=percentage,
            tipType=tip_type
        )
    )


def rest_voucher(card: FiServCard, amount=None):
    s = rest_sale(amount=amount)
    s.paymentMethod = paymentMethod(voucher=voucher(
        cardAccount=card.cardaccount,
        cardNumber=card.cardnum,
        cardType='CBIC',
        voucherApprovalCode='123456',
        voucherNumber='123456789012345'
    ))
    s.requestType = 'PURCHASE'
    s.account.terminalType = 'CHP'
    s.deviceType = 'INGENICO_ICT220'
    return s


def rest_keyed_securecard(merchant_reference=None, cardtype='visa'):
    if not merchant_reference:
        merchant_reference = f'REST_SC_{str(fake.random_number(7, False))}'
    s = secureCard(
        dateTime=today,
        cardEntryMode=cardEntryMode.KEYED,
        merchantReference=merchant_reference,
        tokenMethod=rest_token_method_keyed_secure_card(cardtype),
        customer=customer(
            city=fake.city(),
            country=fake.country(),
            eMail=fake.free_email(),
            ipAddress=fake.ipv4(),
            mobileNumber=str(fake.random_number(digits=10, fix_len=True)),
            region=fake.state(),
        ),
        device=posDevice(
            serialNumber=str(fake.random_number(digits=8, fix_len=True)),
            type_='WISEPAD'
        ),
        deviceType='WISEPAD'
    )
    return s


def rest_token_method_keyed_secure_card(cardtype='visa'):
    card = random_card(cardtype)
    return tokenMethod(keyedSecureCard(
        cardCvv=str(fake.random_number(digits=3)),
        cardNumber=card.cardnumber,
        cardType=cardtype,
        cardHolderName=card.cardholder,
        expiryDate=card.cardexpiry
    ))


def rest_token_method_keyed_as_track2():
    return tokenMethod(keyedAsTrack2=keyedAsTrackData(
        cardType='VISA',
        encryptedData='5923F0A99BA5D8F74D076AFF49D9A6BF49D2E2468A17DA58',
        ksn='88888813710009600123',
        firstDigitOfPan='5'
    ))


def rest_token_method_keyed_encrypted():
    return tokenMethod(keyedEncrypted=keyedEncrypted())


def rest_token_method_track_secure_card():
    return tokenMethod(trackSecureCard=trackData())


def rest_token_method_emv_secure_card():
    return tokenMethod(emvSecureCard=emv())


def rest_token_method_emv_tlv_secure_card():
    return tokenMethod(emvSecureCard=emvtlv())


def rest_sale(amount=None, cardtype='visa', cvv='999'):
    request = sale(
        orderId=f'REST_{str(fake.random_number(7, False))}',
        dateTime=today,
        account=rest_account(),
        amount=rest_amount(amount),
        autoReady='true',
        commerceType=commerceType.NOT_APPLICABLE,
        customer=rest_customer(),
        receiptDetailsRequired=False,
        paymentMethod=paymentMethod(rest_keyed_card(cardtype, cvv))
    )
    request.receiptDetailsRequired = True
    return request


def rest_androidpay_sale(amount=None, currency='USD'):
    request = sale(
        orderId='REST_' + str(fake.random_number(7, False)),
        dateTime=today,
        account=rest_account(),
        amount=rest_amount(amount, currency),
        commerceType=commerceType.NOT_APPLICABLE,
        customer=rest_customer(),
        receiptDetailsRequired=False,
        paymentMethod=paymentMethod(
            androidPay=androidWallet(
                payload='7b22656e637279707465644d657373616765223a22446674506654644f6d56442b4163675038326d5c2f745545756d614872717238717a434b51736c316e6a614f3562796a373345304c3576744d53746b4661786f7758744f57364d47676a47413452685c2f4f57733432654b587a55792b544b31614a4a4968364548637038692b2b6f73507a4449696b3551773230595a7332716452425761794d745974657a6b3644435145386b377a67372b48457663537743337a57394d775155395675506e4455453047325c2f36496a38615465356557443777717152556d6b44456a65564c514178666436516d4c222c22746167223a2241364f773261694453435441553645797834753732716d7a71434632325371597859705c2f4c6c44304438453d222c22657068656d6572616c5075626c69634b6579223a22424b706b6f6e41633934654e635c2f4365334b6b6b6f447171502b786e7555637772786d456f326e66735a664e6751735579354c7a776d674e6749576b6c5a49766f6a674b5a645634764534355c2f4a4832556a434d324a6b3d227d',
                cardholderName=fake.name()
            )
        )
    )
    return request


def rest_applepay_sale(amount=None, currency='USD'):
    request = sale(
        orderId='REST_' + str(fake.random_number(7, False)),
        dateTime=today,
        account=rest_account(),
        amount=rest_amount(amount, currency),
        commerceType=commerceType.NOT_APPLICABLE,
        customer=rest_customer(),
        receiptDetailsRequired=False,
        paymentMethod=paymentMethod(
            applePay=appleWallet(
                payload='7b2276657273696f6e223a2245435f7631222c2264617461223a2266384e54484e664e5156556158732f623473476a4c4b52692b756b5a44416f7045344e734b73715246706a736c33536442334963564a4b6a646d65526f4b38516357724f5835642b584766436e4e414863504f6d7541627845486656344855784778533030345863764d36484958544d6133476a77375a547a72484d5137567970324b35726d774f6b6b70386b426f6a3933567862336857474644736a337274614d4d4d5761692b764b4851307734757034313556644a4473614239375857693445394d71506c46497632574f686430704c6c7665366b67745a5a64543575315a504d2b59596c373448383854317a65637a726f662f6b763271486c6d6651375857384a7a356251564d54663363323136456247426d55796b6e42455a59684f6b78653461364d59446a652b343666304a646e5734736f5773342b4f75697a32505768483176375141655a304e2f575a35524657386758786b314e34426131542f616f3876517954582b71374c636c6a4165687831586158396c72765a36664f61667a376677764e78563043622b314f504a55624945635a6e33686265315376484c6f48777145586649733d222c227369676e6174757265223a224d494147435371475349623344514548417143414d49414341514578447a414e42676c67686b67425a514d45416745464144434142676b71686b69473977304242774541414b43414d494944356a4343413475674177494241674949614744326d646e4d70773877436759494b6f5a497a6a304541774977656a45754d437747413155454177776c51584277624755675158427762476c6a5958527062323467535735305a5764795958527062323467513045674c5342484d7a456d4d435147413155454377776451584277624755675132567964476c6d61574e6864476c76626942426458526f62334a7064486b78457a415242674e5642416f4d436b46776347786c49456c7559793478437a414a42674e5642415954416c56544d423458445445324d4459774d7a45344d5459304d466f58445449784d4459774d6a45344d5459304d466f77596a456f4d43594741315545417777665a574e6a4c584e7463433169636d39725a58497463326c6e626c3956517a51745530464f52454a50574445554d424947413155454377774c6155395449464e356333526c62584d78457a415242674e5642416f4d436b46776347786c49456c7559793478437a414a42674e5642415954416c56544d466b77457759484b6f5a497a6a3043415159494b6f5a497a6a30444151634451674145676a443971384f63393134674c46445a6d305553356a666971514864624c50677363314c556d65592b4d394f766567614a616a43486b777a3363364f4b70624339712b686b774e46784f68365243624f6c5273536c614f43416845776767494e4d45554743437347415155464277454242446b774e7a4131426767724267454642516377415959706148523063446f764c32396a633341755958427762475575593239744c32396a633341774e433168634842735a5746705932457a4d444977485159445652304f424259454641496b4d417561377531474d5a656b706c6f706e6b4a78676878464d41774741315564457745422f7751434d414177487759445652306a42426777466f4155492f4a4a78452b54354f386e357354324b47772f6f7276394c6b73776767456442674e5648534145676745554d4949424544434341517747435371475349623359325146415443422f6a4342777759494b77594242515548416749776762594d67624e535a5778705957356a5a5342766269423061476c7a49474e6c636e52705a6d6c6a5958526c49474a35494746756553427759584a306553426863334e316257567a4947466a593256776447467559325567623259676447686c4948526f5a5734675958427762476c6a59574a735a53427a644746755a4746795a4342305a584a7463794268626d5167593239755a476c3061573975637942765a6942316332557349474e6c636e52705a6d6c6a5958526c4948427662476c6a65534268626d51675932567964476c6d61574e6864476c7662694277636d466a64476c6a5a53427a644746305a57316c626e527a4c6a4132426767724267454642516343415259716148523063446f764c33643364793568634842735a53356a623230765932567964476c6d61574e68644756686458526f62334a7064486b764d44514741315564487751744d4373774b61416e6f43574749326830644841364c79396a636d77755958427762475575593239744c3246776347786c59576c6a59544d7559334a734d41344741315564447745422f775145417749486744415042676b71686b694739324e6b42683045416755414d416f4743437147534d343942414d4341306b414d4559434951446148474f75692b583254343452364756704e376d326e456372365436734d6a4f685a354e75536f316567774968414c31612b2f68703838444b4a3073763365543346785763733731786d624c4b442f514a336d576167724a4e4d494943376a4343416e5767417749424167494953573076767a715932706377436759494b6f5a497a6a3045417749775a7a45624d426b4741315545417777535158427762475567556d397664434244515341744945637a4d5359774a4159445651514c44423142634842735a5342445a584a3061575a7059324630615739754945463164476876636d6c30655445544d424547413155454367774b51584277624755675357356a4c6a454c4d416b474131554542684d4356564d774868634e4d5451774e5441324d6a4d304e6a4d775768634e4d6a6b774e5441324d6a4d304e6a4d77576a42364d5334774c4159445651514444435642634842735a5342426348427361574e6864476c766269424a626e526c5a334a6864476c7662694244515341744945637a4d5359774a4159445651514c44423142634842735a5342445a584a3061575a7059324630615739754945463164476876636d6c30655445544d424547413155454367774b51584277624755675357356a4c6a454c4d416b474131554542684d4356564d775754415442676371686b6a4f5051494242676771686b6a4f50514d4242774e4341415477467847454764646b68645561586957424233626f674b4c76336e75755465434e2f45755434544e5731575a624e613469304a643244534a4f65376f492f5859587a6f6a4c6472746d634c374936436d452f3152466f3448334d4948304d45594743437347415155464277454242446f774f444132426767724267454642516377415959716148523063446f764c32396a633341755958427762475575593239744c32396a633341774e433168634842735a584a766233526a5957637a4d42304741315564446751574242516a386b6e455435506b3779666d7850596f62442b69752f3075537a415042674e5648524d4241663845425441444151482f4d42384741315564497751594d426141464c7577337146594d3469617049715a3372363936362f61797953724d44634741315564487751774d4334774c4b41716f4369474a6d6830644841364c79396a636d77755958427762475575593239744c3246776347786c636d397664474e685a7a4d7559334a734d41344741315564447745422f77514541774942426a415142676f71686b694739324e6b4267494f424149464144414b42676771686b6a4f5051514441674e6e4144426b416a41367a334b445552615a735962374e634e57796d4b2f394266743251393154614b4f767647636756354374346e346d506562575a2b593155454e6a353370777634434d44497431555168734b4d4664327864387a67376b476639463377734957325754385a796159495362315434656e30626d63756243596b685951615a44776d53485141414d594942697a4343415963434151457767595977656a45754d437747413155454177776c51584277624755675158427762476c6a5958527062323467535735305a5764795958527062323467513045674c5342484d7a456d4d435147413155454377776451584277624755675132567964476c6d61574e6864476c76626942426458526f62334a7064486b78457a415242674e5642416f4d436b46776347786c49456c7559793478437a414a42674e5642415954416c56544167686f5950615a3263796e447a414e42676c67686b67425a514d4541674546414b43426c54415942676b71686b69473977304243514d784377594a4b6f5a496876634e415163424d42774743537147534962334451454a42544550467730784e7a41784d7a45784d5451354e5468614d436f4743537147534962334451454a4e4445644d4273774451594a59495a49415755444241494242514368436759494b6f5a497a6a3045417749774c77594a4b6f5a496876634e41516b454d53494549416e5a464775364b723878456c2f67464356596d6a6d5338464449674b485776427841655257436c6272574d416f4743437147534d343942414d434245597752414967597a3059355333614a3238466b6368544c6f636a344a454d744c693567794256564245416a5869644c2b51434944574a576a62594132703054756239712f77616c6b322f723551765870765871554b64365748332f5a4e4d4141414141414141222c22686561646572223a7b22657068656d6572616c5075626c69634b6579223a224d466b77457759484b6f5a497a6a3043415159494b6f5a497a6a3044415163445167414530566232395839514934747059776a2f4d486d31486e666f4179434744474e765575303058646272566d46614e6b336834344a2b3065507435316736586e3847525a74434c6f43472f6b515a71577a567730574c54413d3d222c227075626c69634b657948617368223a22524c7632446b6844683266313032654c615866636558677a417643476c4c6f426f73524a674a376971674d3d222c227472616e73616374696f6e4964223a2232353666303035313061656136303536393263643062383630363362363536353464643065363965643462626539633432386331383234383262656137326533227d7d',
            )
        )
    )
    return request


def rest_track2contactless():
    # WISEPAD device
    # trackdata ;5413330089604111=22122010123409172000?
    return trackDataContactless(
        additionalTags='9F6E06005611123031',
        cardHolderName=fake.name(),
        cardType="MASTERCARD",
        encryptedData="311331E5F10CC9CFFC4D4891A6E103B9A3E01F91D0946901",
        fallback="false",
        ksn="FFFF5678901234E00001"
    )


def rest_emv_tlv_sale(amount=None, currency: Currency = Currency.USD, device_type=PosDevice.WISEPAD.device_name):
    request = sale(
        orderId='REST_' + str(fake.random_number(7, False)),
        dateTime=today,
        account=rest_account(device_type=device_type),
        amount=rest_amount(amount, currency.name),
        commerceType=commerceType.NOT_APPLICABLE,
        customer=rest_customer(),
        receiptDetailsRequired=True,
        device=rest_pos_device(device_type=device_type),
        paymentMethod=paymentMethod(
            emvTlv=emvtlv(
                contactless='true',
                cardType='VISA',
                ksn='88888835400002200001',
                tlvString=EmvTlv.CONTACTLESS_ICC.value
            )
        ),
        deviceType=device_type
    )
    return request


def rest_track2_sale(amount=None, currency: Currency = Currency.USD, device_type=PosDevice.WISEPAD.device_name):
    request = sale(
        orderId='REST_' + str(fake.random_number(7, False)),
        dateTime=today,
        account=rest_account(device_type=device_type),
        amount=rest_amount(amount, currency.name),
        commerceType=commerceType.NOT_APPLICABLE,
        customer=rest_customer(),
        receiptDetailsRequired=True,
        device=rest_pos_device(device_type=device_type),
        paymentMethod=paymentMethod(
            track2=trackData(
                cardType='VISA',
                encryptedData='5923F0A99BA5D8F74D076AFF49D9A6BF49D2E2468A17DA58',
                fallback='false',
                ksn='88888813710009600123'
            )
        ),
        deviceType=device_type
    )
    return request


def rest_securecard_sale(cardreference, amount=None):
    request = sale(
        orderId='REST_' + str(fake.random_number(7, False)),
        dateTime=today,
        account=account(
            deviceId='WALKER',
            operator=fake.name(),
            terminalType=terminalType.INTERNET
        ),
        amount=rest_amount(amount, 'USD'),
        commerceType=commerceType.NOT_APPLICABLE,
        customer=rest_customer(),
        receiptDetailsRequired=True,
        paymentMethod=paymentMethod(
            secureCard=secureCardMethod(
                cardReference=cardreference
            )
        )
    )
    return request


def rest_fiserv_sale(card: FiServCard = None, device_type=PosDevice.WISEPAD.device_name):
    if not card:
        card = FiServCard.rand()

    s = rest_sale()
    s.without_field('customer', 'autoReady')
    s.account.terminalType = 'CHP'
    s.device = rest_pos_device(device_type=device_type)
    s.paymentMethod.keyedCard.cardHolderName = None
    s.paymentMethod.keyedCard.cardType = 'CBIC'
    s.paymentMethod.keyedCard.cardNumber = card.cardnum
    s.paymentMethod.keyedCard.cardAccount = card.cardaccount
    s.paymentMethod.keyedCard.cvv = None
    s.paymentMethod.keyedCard.pinDetails = pinDetails(dukptPinDetails(
        pin=card.pin,
        pinKsn=card.ksn
    ))
    s.requestType = 'PURCHASE'
    return s


def rest_referenced_refund(uniqueref, amount, device_type=PosDevice.WISEPAD.device_name):
    request = refund(
        dateTime=today,
        account=rest_account(),
        amount=rest_amount(amount),
        device=rest_pos_device(device_type=device_type),
        commerceType=commerceType.NOT_APPLICABLE,
        customer=rest_customer(),
        receiptDetailsRequired=False,
        refundMethod=refundMethod(
            referenced=refundReferenced(
                uniqueRef=uniqueref,
                reason=fake.text(20))
        ),
        deviceType=device_type
    )
    return request


def rest_unreferenced_track2_refund(amount, device_type=PosDevice.WISEPAD.device_name):
    request = refund(
        dateTime=today,
        account=rest_account(device_type),
        amount=rest_amount(amount),
        commerceType=commerceType.NOT_APPLICABLE,
        customer=rest_customer(),
        receiptDetailsRequired=False,
        device=rest_pos_device(device_type=device_type),
        refundMethod=refundMethod(
            unreferenced=refundUnreferenced(
                track2=trackData(
                    cardType='VISA',
                    encryptedData='5923F0A99BA5D8F74D076AFF49D9A6BF49D2E2468A17DA58',
                    fallback='false',
                    ksn='88888813710009600123'
                ),
                reason=fake.text(20),
                orderId='REST_' + str(fake.random_number(7, False))
            )
        ),
        deviceType=device_type
    )
    return request


def rest_unreferenced_card_refund(amount=None, cardtype=None, currency=Currency.USD,
                                  device_type=PosDevice.WISEPAD.device_name):
    if not amount:
        amount = random_amount(currency=currency)
    request = refund(
        dateTime=today,
        account=rest_account(device_type=device_type),
        amount=rest_amount(amount),
        commerceType=commerceType.NOT_APPLICABLE,
        device=rest_pos_device(device_type=device_type),
        customer=rest_customer(),
        receiptDetailsRequired=False,
        refundMethod=refundMethod(
            unreferenced=refundUnreferenced(
                cardDetails=rest_card_details(cardtype),
                reason=fake.text(20),
                orderId='REST_' + str(fake.random_number(7, False))
            )
        ),
        deviceType=device_type
    )
    return request


def rest_reversal(uniqueref, device_type=PosDevice.WISEPAD.device_name):
    return reversal(
        dateTime=today,
        account=rest_account(device_type=device_type),
        customer=rest_customer(),
        uniqueRef=uniqueref,
        deviceType=device_type,
        reason=fake.text(15)
    )


def rest_taxes(*args: tax):
    return taxesType(tax=args)


def rest_tip(amount, tip_type: tipType = tipType.FIXED_AMOUNT, currency: Currency = Currency.USD):
    return tip(
            tipType=tip_type,
            currency=currency.name,
            amount_member=amount
    )


def rest_balance_inquiry(currency: Currency = Currency.USD):
    return balanceInquiry(
        currency=currency.name,
        account=rest_account(),
        dateTime=today,
        deviceType='WISEPAD',
        cardReadMethod=paymentMethod(rest_keyed_card())
    )


def rest_transaction_update(device_type=PosDevice.WISEPAD.device_name):
    return transactionUpdate(
        dateTime=datetime.now().replace(microsecond=0),
        deviceType=device_type,
        account=rest_account(device_type=device_type)
    )
