from faker import Factory

from model.boarding import user as user_, userProcessingTerminalsType
from constants import TimeZone

fake = Factory.create()


def user(merchant_id=None, user_name='user', terminals=list):
    return user_(
        userName=user_name,
        merchantId=merchant_id,
        userEmail=fake.free_email(),
        timeZone=TimeZone.LONDON.timezone,
        allowTerminalSetup=True,
        allowPaymentPageLayout=True,
        allowRefund=True,
        allowUnreferencedRefunds=True,
        allowVirtualTerminal=True,
        allowChpOnVt=False,
        allowUserSetup=True,
        allowOpenBatch=True,
        allowClosedBatch=True,
        allowBulkPaymentsResults=True,
        allowBilling=True,
        allowPreauth=True,
        allowSecureCards=True,
        allowSubscriptions=True,
        allowDashboard=False,
        allowAchjhtransactions=True,
        allowPartialCaptures=True,
        allowScheduledReport=True,
        userProcessingTerminals=userProcessingTerminalsType(terminals))
