from faker import Factory
from hamcrest import assert_that, equal_to, instance_of
from model.gateway import SEND_PAYMENT_LINK_EMAIL_RESPONSE, ERROR, CREATE_PAYMENT_LINK_RESPONSE
from wnclient import WNClient

wn = WNClient().vagrant.go
fake = Factory.create()

TERM_ID = '21001'


def test_payment_link_send_with_empty_email_body():
    create_response = wn.xml(TERM_ID).payment_link_create()
    assert_that(create_response, instance_of(CREATE_PAYMENT_LINK_RESPONSE))

    response = wn.xml(TERM_ID).payment_link_send(create_response.MERCHANTREF)
    assert_that(response, instance_of(SEND_PAYMENT_LINK_EMAIL_RESPONSE))
    assert_that(response.MERCHANTREF, equal_to(create_response.MERCHANTREF))


def test_payment_link_send_with_filled_email_body():
    EMAIL_BODY = '''<![CDATA[
            <!DOCTYPE html>
            <html>
              <body bgcolor="#f9f9f9" style="margin: 0; padding: 0; background:#f9f9f9">
                {PAYNOWBUTTON}
                <table style="width: 100%;">
                  <tbody>
                    <tr>
                      <td height="20"></td>
                    </tr>
                  </tbody>
                </table>
                <table style="line-height: 135%; border-radius: 3px 3px 0 0; max-width: 580px; width: 100%; margin: 0 auto;" bgcolor="#ffffff">
                  <tbody>
                    <tr>
                      <td>
                        <table border="0" cellpadding="0" cellspacing="10" style="width: 100%;">
                          <tbody>
                            <tr>
                              <td align="right">
                                <div style="color: #042029; font-size: 1.3em; font-weight:100; margin: 0;">
                                  <img src="https://www.freelogodesign.org/img/logo-ex-7.png" alt="Logo">
                                </div>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                        <table border="0" cellpadding="0" cellspacing="10" style="width: 100%;">
                          <tbody>
                            <tr>
                              <td>Order XXXXXX</td>
                            </tr>
                            <tr>
                              <td>Reference:</td>
                            </tr>
                            <tr>
                              <td>Garden Services</td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </body>
            </html>
        ]]>'''

    create_response = wn.xml(TERM_ID).payment_link_create()
    assert_that(create_response, instance_of(CREATE_PAYMENT_LINK_RESPONSE))

    response = wn.xml(TERM_ID).payment_link_send(create_response.MERCHANTREF)
    assert_that(response, instance_of(SEND_PAYMENT_LINK_EMAIL_RESPONSE))
    assert_that(response.MERCHANTREF, equal_to(create_response.MERCHANTREF))


def test_payment_link_send_link_not_exists():
    response = wn.xml(TERM_ID).payment_link_send(merchantref='123')
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Invoice Payment Request does not exist'))


def test_payment_link_send_link_already_processed():
    pass