import os

from constants import ApiKey
from wnclient import WNClient

wn = WNClient().vagrant.wn.rest2()
db = WNClient().db()
WN_KEY = ApiKey.API_WN_FULL

key = db.get_api_key(WN_KEY)
auth = wn.authenticate(key, silence=False)

bapi_scheme_url = 'https://vagrant.wntps.com/merchant/api/v1/docs/openapi.yaml'
rest2_args = ["schemathesis", "run", "--stateful=links", "-c", "all", bapi_scheme_url,
              "--validate-schema=false",
              "--request-tls-verify=false", "-H", "\"Authorization: Bearer %s\"" % auth.token,
              "-H", "\"Content-Type: application/json\"",
              "-H", "\"Accept: application/json\""]
print(' '.join(rest2_args))
r = os.popen(' '.join(rest2_args)).read()
print(r)

