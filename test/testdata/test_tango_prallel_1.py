from time import sleep

import pytest
from faker import Factory
from hamcrest import assert_that, instance_of

from constants import Currency
from data.xml_requests import payment
from model.gateway import PAYMENTRESPONSE
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
TERM_ID = '21004'
VISA_EDCC = '4485910301709438'  # GPB > USD

# pip3 install pytest-repeat
# pytest-repeat is a plugin for pytest that makes it easy to repeat a single test, or multiple tests, a specific number of times.
# pip3 install pytest-xdist
# python3 -m pytest -n 2 /home/mf/repos/wnapi2/test/xml/acquirer/tango/test_tango_prallel_1.py::test_tango_moto_approved_payment1


@pytest.mark.repeat(1)
def test_tango_moto_approved_payment1():
    sleep(1)
    p = payment()
    p.CURRENCY = Currency.CAD.name
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
