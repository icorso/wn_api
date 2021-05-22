from time import sleep

import pytest
from faker import Factory

from constants import ApiKey
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.wn
TERM_ID = '22005'
# pip3 install pytest-repeat
# pytest-repeat is a plugin for pytest that makes it easy to repeat a single test, or multiple tests, a specific number of times.
# pip3 install pytest-xdist
# python3 -m pytest -n 2 /home/mf/repos/wnapi2/test/xml/acquirer/tango/test_tango_prallel_1.py::test_tango_moto_approved_payment1
db = WNClient().db()

KEY = db.get_api_key(ApiKey.API_WN_FULL)


@pytest.mark.repeat(2)
def test_fdrc_refund1():
    # payment_response = wn.xml(terminal_id=TERM_ID).payment()
    uniqueref = 'K4VSJSSXB6'
    amount = 5.28
    # refund_response = wn.xml(terminal_id=TERM_ID).refund(uniqueref, amount=5.28, currency=Currency.USD)
    refund_response = wn.rest2(terminal_id=TERM_ID).payment_refund(uniqueref, amount=amount, api2_key=KEY)
    print(refund_response.json())
    sleep(1)
