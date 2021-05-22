from copy import deepcopy

from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import LocalMerchant, CARDTYPES, ApiKey
from data.boarding.terminal import fdrc_terminal
from model.boarding import terminal, cardsType
from model.boarding2 import FdrcTerminal
from model.boarding2 import FiServTerminal
from model.rest import paymentTypeEnum
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.wn.boarding()
wn_boarding2 = WNClient().vagrant.goepay.boarding2()
db = WNClient().db()

FDRC_TERM_ID = '22004'
FISERV_TERM_ID = '22003'
MERCHANT_ID = LocalMerchant.WN.itemid


def test_boarding_terminal_fdrc_create_and_get():
    t = fdrc_terminal(merchant_id=MERCHANT_ID)
    response = wn.create_terminal(request=t)
    assert_that(response, instance_of(terminal))

    get_terminal = wn.get_terminal(response.terminalNumber)
    assert_that(get_terminal, instance_of(terminal))
    assert_that(sorted(get_terminal.cards.card), equal_to(sorted(CARDTYPES)))


def test_boarding_terminal_fdrc_has_secondary_fiserv_update():
    key = db.get_api_key(ApiKey.BOARDING_WN_FULL)
    wn_boarding2.update_processing_rules(merchant_id=MERCHANT_ID, terminal_number=FISERV_TERM_ID, response_type=FiServTerminal,
                                         to_terminal=FDRC_TERM_ID, boarding2_key=key)
    wn_boarding2.update_processing_rules(merchant_id=MERCHANT_ID, terminal_number=FDRC_TERM_ID, response_type=FdrcTerminal,
                                         value=paymentTypeEnum.EBT, to_terminal=FISERV_TERM_ID, boarding2_key=key)

    fdrc_terminal_response = wn.get_terminal(terminal_number=FDRC_TERM_ID)

    cards = deepcopy(CARDTYPES)
    cards.remove('SHELL')
    new_cards = sorted(cards)
    fdrc_terminal_response.cards = cardsType(new_cards)
    assert_that(fdrc_terminal_response, instance_of(terminal))

    fdrc_terminal_update = wn.update_terminal(fdrc_terminal_response)
    assert_that(fdrc_terminal_update, instance_of(terminal))
    assert_that(sorted(fdrc_terminal_update.cards.card), equal_to(new_cards))

    fdrc_terminal_response.cards = cardsType(CARDTYPES)
    wn.update_terminal(fdrc_terminal_response)
