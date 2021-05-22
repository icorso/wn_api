import json

import deepdiff
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import LocalMerchant, ApiKey, Country, TimeZone
from model.boarding2 import PaynomixTerminal, PaynomixBankSettings, TerminalLocationDetails, TerminalFeatures, \
    PaynomixFeatures, SecureCredentials
from wnclient import WNClient

wn = WNClient().vagrant.wn.boarding2()
db = WNClient().db()
WN_KEY = ApiKey.BOARDING_WN_FULL
fake = Factory().create()


def test_tsys_saratoga_create_terminal_valid():
    p = PaynomixTerminal(
        payment_processor='Paynomix',
        secret='someSecretPhrase',
        terminal_location=TerminalLocationDetails(
            country=Country.Ireland.short_code,
            time_zone=TimeZone.LONDON.timezone
        ),
        bank_settings=PaynomixBankSettings(
            base_currency='USD',
            merchant_api_key=fake.msisdn(),
            allow_internet=True,
            allow_pre_auth=True
        ),
        terminal_features=PaynomixFeatures(
            allow_virtual_terminal_auto_order_id=True,
            allow_bulk_payments=True,
            secure_credentials=SecureCredentials(
                allow_subscriptions=True,
                enable_secure_card_validation=True
            )
        )
    )

    wn_key = db.get_api_key(WN_KEY)
    response = wn.create_terminal(LocalMerchant.WN.itemid, p, PaynomixTerminal, wn_key, silence=False)
    assert_that(response, instance_of(PaynomixTerminal))
    new_terminal = wn.get_terminal(LocalMerchant.WN.itemid, response.terminal_number, PaynomixTerminal, wn_key)

    p.terminal_number = new_terminal.terminal_number
    p.secret = None
    diff = json.dumps(
        json.loads(
            deepdiff.DeepDiff(p.to_dict(), new_terminal.to_dict()).to_json()
        ), indent=4)
    print(diff)
    assert_that(diff, equal_to('{}'))
