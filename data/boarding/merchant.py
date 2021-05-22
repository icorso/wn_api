from faker import Factory

from constants import Country, TimeZone
from model.boarding import merchant as merchant_, pricingTypeEnum, monthlyFeeTypeEnum, pricing as pricing_, \
    standardTransactionClassificationEnum

fake = Factory.create()


def pricing():
    return pricing_(
        monthlyFee=fake.pyfloat(left_digits=2, right_digits=1, positive=True),
        monthlyFeeType=monthlyFeeTypeEnum.INCLUDED_TRANS,
        monthlyIncludedStandardTransactions=fake.random_int(1, 20),
        perStandardTxnFee=fake.pyfloat(left_digits=1, right_digits=1, positive=True),
        perThreedTxnFee=fake.pyfloat(left_digits=2, right_digits=1, positive=True),
        perEdccTxnFee=fake.pyfloat(left_digits=1, right_digits=1, positive=True),
        perSecureCardTxnFee=fake.pyfloat(left_digits=2, right_digits=1, positive=True),
        perSmsFee=fake.pyfloat(left_digits=1, right_digits=1, positive=True),
        maxMindRequestFee=fake.pyfloat(left_digits=2, right_digits=1, positive=True),
        maxMindRejectionFee=fake.pyfloat(left_digits=1, right_digits=1, positive=True),
        standardTransactionClassification=standardTransactionClassificationEnum.ALL
    )


def merchant(merchant_portfolio, host='wn', dba_name=None, ):
    if not dba_name:
        dba_name = fake.name()
    return merchant_(
        gatewayHost=host,
        dbaName=dba_name,
        contact=fake.name(),
        phone=fake.msisdn(),
        email=fake.free_email(),
        city=fake.city(),
        mcc=str(fake.random_number(4, True)),
        address1=fake.street_address(),
        address2=fake.secondary_address(),
        address3=fake.license_plate(),
        country=Country.Russia.code,
        timeZone=TimeZone.MOSCOW.timezone,
        pricingType=pricingTypeEnum.MERCHANT_LEVEL,
        merchantPricing=pricing(),
        merchantPortfolioUniqueId=merchant_portfolio

    )
