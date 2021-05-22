import hashlib
import random

from faker import Factory

from constants import SecCode, AccountType, RoutingNumber, Currency, StoredCredentialTxType, StoredCredentialUse, \
    SecureCardAchJh, SecureCard
from utils import today, random_amount, random_card, random_text

fake = Factory.create()


def gen_hash(input_string: str, is_old_hash=False):
    m = hashlib.sha512()
    if is_old_hash:  # the string should be w/o a separator
        m = hashlib.md5()
    m.update(str.encode(input_string))
    return m.hexdigest()


def generate_ach_bulk_payment_csv(count=1, terminal_id='21001', secret='someSecretPhrase'):
    # ORDERID,CURRENCY,AMOUNT,ACH_SECURE,SEC_CODE,ACCOUNT_TYPE,ACCOUNT_NUMBER, ROUTING_NUMBER,ACCOUNT_NAME,CHECK_NUMBER
    # DL_STATE,DL_NUMBER,ADDRESS1,ADDRESS2,CITY,REGION,COUNTRY,POSTCODE, PHONE,DATETIME,HASH,DESCRIPTION,EMAIL
    rows = []
    hash_string = ""
    currency = Currency.USD
    for i in range(count):
        order_id = 'BLK' + str(fake.random_number(6, True))
        bulk_date = today()
        # hash_string = terminal_id + ':' + order_id + ':' + amount + ':' + bulk_date + ':' + secret
        rows.append([order_id, currency.name, str(random_amount(currency=currency)), 'N', SecCode.rand(), AccountType.rand().description,
                     str(fake.random_number(17, True)),
                     RoutingNumber.rand_rn(), fake.company(), str(fake.random_number(17)), fake.state_abbr(), fake.license_plate(),
                     fake.street_address(), fake.secondary_address(), fake.city(), fake.state(), fake.country_code(), fake.postcode(),
                     fake.phone_number(), bulk_date])

    csv_file = ''
    total_amount = 0.0
    for c in rows:
        hash_string = str(terminal_id) + ':' + str(c[0]) + ':' + str(c[2]) + ':' + c[19] + ':' + secret
        csv_file += ('"' + '","'.join(c))
        csv_file = csv_file + '",' + gen_hash(hash_string, False) + ',"' + fake.text(30) + '","' + fake.free_email() + '"\n'
        total_amount += float(c[2])

    with open("/home/mf/Desktop/ach_bulk_%stxn_%samount.csv" % (count, total_amount), "w") as text_file:
        text_file.write(csv_file)

    return [count, total_amount, csv_file, hash_string]


def generate_ach_secure_bulk_payment_csv(cardreference, count=1, terminal_id='21001', secret='someSecretPhrase'):
    # ORDERID,CURRENCY,AMOUNT,ACH_SECURE,SEC_CODE,ACCOUNT_TYPE,ACCOUNT_NUMBER, ROUTING_NUMBER,ACCOUNT_NAME,CHECK_NUMBER
    # DL_STATE,DL_NUMBER,ADDRESS1,ADDRESS2,CITY,REGION,COUNTRY,POSTCODE, PHONE,DATETIME,HASH,DESCRIPTION,EMAIL
    rows = []
    hash_string = ""
    currency = Currency.USD
    for i in range(count):
        order_id = 'BLK' + str(fake.random_number(6, True))
        bulk_date = today()
        # hash_string = terminal_id + ':' + order_id + ':' + amount + ':' + bulk_date + ':' + secret
        rows.append([order_id, currency.name, str(random_amount(currency=currency)), 'Y', SecCode.rand(), AccountType.rand().description,
                     cardreference, RoutingNumber.rand_rn(), fake.company(), str(fake.random_number(17)), fake.state_abbr(), fake.license_plate(),
                     fake.street_address(), fake.secondary_address(), fake.city(), fake.state(), fake.country_code(), fake.postcode(),
                     fake.phone_number(), bulk_date])

    csv_file = ''
    total_amount = 0.0
    for c in rows:
        hash_string = str(terminal_id) + ':' + str(c[0]) + ':' + str(c[2]) + ':' + c[19] + ':' + secret
        csv_file += ('"' + '","'.join(c))
        csv_file = csv_file + '",' + gen_hash(hash_string, False) + ',"' + fake.text(30) + '","' + fake.free_email() + '"\n'
        total_amount += float(c[2])

    with open("/home/mf/Desktop/ach_bulk_securecard_%stxn_%samount.csv" % (count, total_amount), "w") as text_file:
        text_file.write(csv_file)

    return [count, total_amount, csv_file, hash_string]


def generate_bulk_payment_csv(count=1, terminal_id='21001', cardtype=None, secret='someSecretPhrase', is_header=False):
    # #ORDERID,CURRENCY,AMOUNT,CARDNUMBER,CARDTYPE,CARDEXPIRY,CARDHOLDERNAME,ADDRESS1,ADDRESS2,POSTCODE,DATETIME,HASH,
    # AUTOREADY,DESCRIPTION,EMAIL,ORIGINALBRANDTXIDENTIFIER,STOREDCREDENTIALTXTYPE,STOREDCREDENTIALUSE
    rows = []
    hash_string = ""
    cards = []
    header = 'ORDERID,CURRENCY,AMOUNT,CARDNUMBER,CARDTYPE,CARDEXPIRY,CARDHOLDERNAME,ADDRESS1,ADDRESS2,POSTCODE,DATETIME,HASH,AUTOREADY,DESCRIPTION,EMAIL,ORIGINALBRANDTXIDENTIFIER,STOREDCREDENTIALTXTYPE,STOREDCREDENTIALUSE'
    for c in range(count):
        cards.append(random_card(cardtype=cardtype))

    for i in cards:
        cardnumber = i.cardnumber
        cardtype = i.cardtype
        cardexpiry = i.cardexpiry
        cardholder = i.cardholder
        currency = ['USD']
        cardtype = 'AMEX' if cardtype in 'American' else cardtype
        amount = random_amount()

        order_id = 'BLK' + str(fake.random_number(7, True))
        bulk_date = today()
        # hash_string = terminal_id + ':' + order_id + ':' + amount + ':' + bulk_date + ':' + secret
        rows.append([order_id, random.choice(currency), str(amount), cardnumber, cardtype, cardexpiry,
                     cardholder, fake.street_address(), fake.secondary_address(), fake.postcode(), bulk_date])
    csv_file = ''
    if is_header:
        csv_file = header + '\n'
    total_amount = 0.0
    for c in rows:
        # cof_data = '",'
        # cof_data = '","' + StoredCredentialUse.rand().name
        # cof_data = '","","' + StoredCredentialTxType.rand().name + '","' + StoredCredentialUse.UNSCHEDULED.name
        # cof_data = '","","' + StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN.name + '","' + StoredCredentialUse.INSTALLMENT.name
        # full cof data
        cof_data = '","","' + StoredCredentialTxType.SUBSEQUENT_CARDHOLDER_INITIATED_TXN.name + '","",'
        custom_fields = '"CustomString|%s","CustomNumeric|%s","CustomBoolean|%s"' % \
                        (fake.text(30), str(fake.random_number(4)), str(random.choice([True, False])))
        # TERMINALID:ODERID:AMOUNT:DATETIME:SECRET
        hash_string = terminal_id + ':' + c[0] + ':' + c[2] + ':' + c[10] + ':' + secret
        print(hash_string)
        csv_file += ('"' + '","'.join(c))
        csv_file = csv_file + '",' + gen_hash(hash_string, False) + ',"Y","' + fake.text(30) + '","' \
                   + fake.free_email() + cof_data + custom_fields + '\n'
        total_amount += float(c[2])

    with open("/home/mf/Desktop/bulk_%stxn_%s.csv" % (count, total_amount), "w") as text_file:
        text_file.write(csv_file)

    return [count, total_amount, csv_file, hash_string]


def generate_bulk_securecard_payment(cardnumber, currency=Currency.GBP, count=1, terminal_id='22001', secret='someSecretPhrase', is_header=False):
    # ORDERID,CURRENCY,AMOUNT,CARDNUMBER,CARDTYPE,ADDRESS1,ADDRESS2,POSTCODE,DATETIME,HASH,
    # AUTOREADY,DESCRIPTION,EMAIL,ORIGINALBRANDTXIDENTIFIER,STOREDCREDENTIALTXTYPE,STOREDCREDENTIALUSE,<CUSTOMFIELDNAME|VALUE>
    # "ODERID","CURRENCY","AMOUNT","CARDNUMBER","CARDTYPE","CARDEXPIRY","CARDHOLDERNAME","ADDRESS1","ADDRESS2","POSTCODE","DATETIME","HASH","AUTOREADY","DESCRIPTION","EMAIL","ORIGINALBRANDTXIDENTIFIER","STOREDCREDENTIALTXTYPE","STOREDCREDENTIALUSE"
    # request hash
    # TERMINALID:ODERID:AMOUNT:DATETIME:SECRET
    # 21001,BLKSC564827,9.52,28-10-2019:10:58:48:000,secret

    # response hash
    # TERMINALID: ORDERID:AMOUNT: DATETIME:RESPONSECODE: RESPONSETEXT:SECRET
    # response HASH = 21001:BLK460012:3.75:24-10-2019:16:25:03:496:A:APPROVAL:someSecretPhrase'
    rows = []
    hash_string = ""

    cardtype = 'SECURECARD'

    for i in range(count):
        amount = random_amount()
        order_id = 'BLKSC' + str(fake.random_number(6, True))
        bulk_date = today()

        # hash_string = terminal_id + ':' + order_id + ':' + amount + ':' + bulk_date + ':' + secret
        rows.append([order_id, currency.name, str(amount), cardnumber, cardtype, '', '', fake.street_address(),
                     fake.secondary_address(), fake.postcode(), bulk_date])
    csv_file = ''
    header = 'ORDERID,CURRENCY,AMOUNT,CARDNUMBER,CARDTYPE,CARDEXPIRY,CARDHOLDERNAME,ADDRESS1,ADDRESS2,POSTCODE,' \
             'DATETIME,HASH,AUTOREADY,DESCRIPTION,EMAIL,ORIGINALBRANDTXIDENTIFIER,STOREDCREDENTIALTXTYPE,STOREDCREDENTIALUSE'
    if is_header:
        csv_file = header + '\n'

    total_amount = 0.0
    for c in rows:
        cof_data = '","' + random_text() + '","' + StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN.name \
                + '","' + StoredCredentialUse.RECURRING.name
        # cof_data = '","","' + StoredCredentialTxType.SUBSEQUENT_CARDHOLDER_INITIATED_TXN.name + '","'
        # cof_data = '","","' + StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN.name + '","' + StoredCredentialUse.RECURRING.name
        # cof_data = '","","","'
        hash_string = terminal_id + ':' + c[0] + ':' + c[2] + ':' + c[10] + ':' + secret

        csv_file += ('"' + '","'.join(c))
        # csv_file = csv_file + '",' + gen_hash(hash_string, False) + ',"Y","' + fake.text(30) + '","' + fake.free_email() + cof_data + '"\n'
        csv_file = csv_file + '","' + gen_hash(hash_string, False) + '","Y","' + fake.text(30) + '","' + fake.free_email() + cof_data + '"\n'
        total_amount += float(c[2])

    with open("/home/mf/Desktop/sc_bulk_%stxn_%samount.csv" % (count, total_amount), "w") as text_file:
        text_file.write(csv_file)

    return [count, total_amount, csv_file, hash_string]


# print(generate_ach_secure_bulk_payment_csv(SecureCardAchJh.ACH_CHECKING.card_ref, count=1))
# print(generate_ach_secure_bulk_payment_csv(SecureCardAchJh.ACH_SAVING.card_ref, count=1))
# print(generate_ach_bulk_payment_csv(2))
generate_bulk_payment_csv(count=2, terminal_id='21001', is_header=False)
# print(generate_bulk_securecard_payment(terminal_id='22014', cardnumber='2967530527860210', count=1, is_header=True))
# print(gen_hash('21002:BLK717090:USD:6.83:29-10-2019:11:41:35:504:A:APPROVAL:someSecretPhrase', False))
