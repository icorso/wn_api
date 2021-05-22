from collections import namedtuple

import requests

from actions import XmlSource, RestSource, BoardingSource, HttpSource, DatabaseSource, HppSource, PayLinkSource
from boarding2_actions import Boarding2Source
from rest2_actions import Rest2Source
from utils import build_url


class HttpSession:
    def __init__(self):
        self._data = None
        self._headers = {}
        self._method = 'post'
        self._session = requests.Session()
        self._response = None
        self._url = None
        self._allow_redirects = True
        self._params = None

    @property
    def request(self):
        response = self._session.request(url=self._url,
                                         headers=self._headers, data=self._data,
                                         allow_redirects=self._allow_redirects,
                                         json=self._data,
                                         method=self._method,
                                         params=self._params,
                                         verify=False)
        return response

    @property
    def url(self):
        return self._url

    @property
    def headers(self):
        return self._headers

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value

    @property
    def session(self):
        return self._session

    @property
    def method(self):
        return self._method

    def with_data(self, data):
        self._data = data
        return self

    def with_params(self, params):
        self._params = params
        return self

    def with_headers(self, headers):
        self._headers.update(headers)
        return self

    def with_session(self, session):
        self._session = session
        return self

    def with_method(self, method):
        self._method = method
        return self

    def with_url(self, url):
        self._url = url
        return self

    def allow_redirects(self, allow_redirects):
        self._allow_redirects = allow_redirects
        return self

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "<HttpSession(url='%s', method='%s', data=%s', headers='%s')>" \
               % (self._url, self._method, self._data, self._headers)


class WNClient(object):
    def __init__(self, terminal_secret=None):
        self._terminal_secret = terminal_secret if terminal_secret else 'someSecretPhrase'
        self._session = HttpSession()
        self._source = None

        self.__init_acquirer = namedtuple('Acquirer', 'wn, go, ncb, pago, ac, goepay, payconex')
        self.__init_gateway = namedtuple('Gateway', 'url, apikey')
        self.__wn = 'wn'
        self.__go = 'go'
        self.__ncb = 'ncb'
        self.__pago = 'pago'
        self.__ac = 'ac'
        self.__goepay = 'goepay'
        self.__payconex = 'payconex'

        self.__scheme = 'http'
        self.__netloc = self.__wn + ':8080'
        self.__path = ''
        self.__url = build_url()

        self.__gateway = self.__init_gateway(self.url, 'wn')
        self.__acquirer = None

    def get_terminal_secret(self):
        return self._terminal_secret

    @property
    def local(self):
        url = '%s:8080'
        self.__acquirer = self.__init_acquirer(
            wn=self.__init_gateway(build_url(netloc=url % self.__wn), 'wnkey'),
            go=self.__init_gateway(build_url(netloc=url % self.__go), 'gokey'),
            ncb=self.__init_gateway(build_url(netloc=url % self.__ncb), 'ncbkey'),
            pago=self.__init_gateway(build_url(netloc=url % self.__pago), 'pagokey'),
            ac=self.__init_gateway(build_url(netloc=url % self.__ac), 'ackey'),
            goepay=self.__init_gateway(build_url(netloc=url % self.__goepay), 'goepaykey'),
            payconex=self.__init_gateway(build_url(netloc=url % self.__payconex), 'payconexkey')
        )
        return self

    @property
    def hound(self):
        url = 'qawshound%s.worldnettps.com'
        self.__acquirer = self.__init_acquirer(
            wn=self.__init_gateway(build_url('https', url % self.__wn), 'a8635d31d3487a2791f587ecf35dbad136878e02d8e1ee563fbdb84975f5f5e11fe706f8bfe64e0a60f419e9b8213a84bb2d5cf8d90ebae3b489d51bdcac6bca'),
            go=self.__init_gateway(build_url('https', url % self.__go), '646a42a9dfd81e1758330b6aedfb48f4d94dee597a50771a96fc5f842c8e722727a254c3382233178172ed72b08166f0c80b027888f55a0265cef992ee73e6f5'),
            ncb=self.__init_gateway(build_url('https', url % self.__ncb), 'houndncbkey'),
            pago=self.__init_gateway(build_url('https', url % self.__pago), 'a685be9b2884743fe7bea1b7a6550d39759e50d542eaf8cf57a8a59668c21b9accaac65c8c2d69c0571b1ef3c2c78b8d6b0f8e2c088e660997deb512c9388747'),
            ac=self.__init_gateway(build_url('https', url % self.__ac), 'ecbc86855a221513220370dbed11df7282ae51e1371c4411805ea30920470d0ed76594b5d8c039987088138a5d022edb08886fea2fcd0fc9a3ca2927110aa487'),
            goepay=self.__init_gateway(build_url('https', url % 'cd'), '50ffd31ef53988da105d9f09b414ffcfcc76aa474441a1596561ad7b74784ce1db39b6f5e8d73f338505703ea401544fe74ff4b90fabbc34b0a92d9665c768a2'),
            payconex=self.__init_gateway(build_url('https', url % self.__payconex), '')
        )
        return self

    @property
    def iron(self):
        url = 'qawsiron%s.worldnettps.com'
        self.__acquirer = self.__init_acquirer(
            wn=self.__init_gateway(build_url('https', url % self.__wn), '883d77cd2c1ebf9cff4b266f219cf64093f5a48b956323d81c63b9421fd70901e6fc88d85f3466ca1bcab4951d75577dae59962c3120ccf0a6fe443fe852dee1'),
            go=self.__init_gateway(build_url('https', url % self.__go), '883d77cd2c1ebf9cff4b266f219cf64093f5a48b956323d81c63b9421fd70901e6fc88d85f3466ca1bcab4951d75577dae59962c3120ccf0a6fe443fe852dee1'),
            ncb=self.__init_gateway(build_url('https', url % self.__ncb[1:]), 'ironncbkey'),
            pago=self.__init_gateway(build_url('https', url % self.__pago), 'ironpagokey'),
            ac=self.__init_gateway(build_url('https', url % self.__ac), 'ironackey'),
            goepay=self.__init_gateway(build_url('https', url % self.__goepay), 'irongoepaykey'),
            payconex=self.__init_gateway(build_url('https', url % self.__payconex), '')
        )
        return self

    @property
    def lynx(self):
        url = 'qawslynx%s.worldnettps.com'
        self.__acquirer = self.__init_acquirer(
            wn=self.__init_gateway(build_url('https', url % self.__wn), 'lynxwnkey'),
            go=self.__init_gateway(build_url('https', url % self.__go), 'lynxgokey'),
            ncb=self.__init_gateway(build_url('https', url % self.__ncb[1:]), 'lynxncbkey'),
            pago=self.__init_gateway(build_url('https', url % self.__pago), 'lynxpagokey'),
            ac=self.__init_gateway(build_url('https', url % self.__ac), 'lynxackey'),
            goepay=self.__init_gateway(build_url('https', url % self.__goepay), 'lynxgoepaykey'),
            payconex = self.__init_gateway(build_url('https', url % self.__payconex), '')
        )
        return self

    @property
    def vagrant(self):
        url = '%s.wntps.com'
        self.__acquirer = self.__init_acquirer(
            wn=self.__init_gateway(build_url('https', url % 'vagrant'), 'wnkey'),
            go=self.__init_gateway(build_url('https', url % 'lpivotal'), 'gokey'),
            ncb=self.__init_gateway(build_url('https', url % 'mobilepayments-jncb-com'), 'ncbkey'),
            pago=self.__init_gateway(build_url('https', url % self.__pago), 'pagokey'),
            ac=self.__init_gateway(build_url('https', url % self.__ac), 'ackey'),
            goepay=self.__init_gateway(build_url('https', url % self.__goepay), 'goepaykey'),
            payconex=self.__init_gateway(build_url('https', url % self.__payconex), 'payconexkey')
        )
        return self

    @property
    def wn(self):
        self.__gateway = self.__acquirer.wn
        return self

    @property
    def go(self):
        self.__gateway = self.__acquirer.go
        return self

    @property
    def ncb(self):
        self.__gateway = self.__acquirer.ncb
        return self

    @property
    def pago(self):
        self.__gateway = self.__acquirer.pago
        return self

    @property
    def ac(self):
        self.__gateway = self.__acquirer.ac
        return self

    @property
    def goepay(self):
        self.__gateway = self.__acquirer.goepay
        return self

    @property
    def payconex(self):
        self.__gateway = self.__acquirer.payconex
        return self

    @property
    def gateway(self):
        return self.__gateway

    def with_gateway(self, gateway_name: str):
        self.__gateway = getattr(self.__acquirer, gateway_name)
        return self

    def xml(self, terminal_id, **kwargs):
        return XmlSource(terminal_id=terminal_id,
                         session=self._session.with_url(self.gateway.url), **kwargs)

    def paylink(self, terminal_id):
        return PayLinkSource(terminal_id=terminal_id, session=self._session.with_url(self.gateway.url))

    def hpp(self, terminal_id):
        return HppSource(terminal_id=terminal_id, session=self._session.with_url(self.gateway.url))

    def rest(self, terminal_id, content_type='json'):
        headers = {'Content-Type': 'application/%s' % content_type}
        return RestSource(terminal_id=terminal_id, session=self._session.with_url(self.gateway.url).with_headers(headers))

    def boarding(self, content_type='xml'):
        headers = {'Content-Type': 'application/%s' % content_type, 'Accept': 'application/%s' % content_type,
                   'AuthenticationKey': self.gateway.apikey}
        return BoardingSource(session=self._session.with_url(self.gateway.url).with_headers(headers))

    def boarding2(self):
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        return Boarding2Source(session=self._session.with_url(self.gateway.url).with_headers(headers))

    def rest2(self, terminal_id=None):
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        return Rest2Source(terminal_id=terminal_id, session=self._session.with_url(self.gateway.url).with_headers(headers))

    def db(self, **kwargs):
        return DatabaseSource(**kwargs)

    @property
    def http(self):
        return HttpSource(session=self._session.with_url(self.gateway.url))

    @property
    def session(self):
        return self._session

    @session.setter
    def session(self, value):
        self._session = value

    @property
    def netloc(self):
        return self.__netloc

    @netloc.setter
    def netloc(self, value):
        self.__netloc = value

    def with_netloc(self, netloc):
        self.__netloc = netloc
        return self

    @property
    def scheme(self):
        return self.__scheme

    @scheme.setter
    def scheme(self, value):
        self.__scheme = value

    def with_scheme(self, scheme):
        #  file, ftp, gopher, hdl, http, https, imap, mailto, mms, news, nntp, prospero, rsync, rtsp, rtspu, sftp,
        # shttp, sip, sips, snews, svn, svn+ssh, telnet, wais, ws, wss
        self.__scheme = scheme
        return self

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        self.__path = value

    def with_path(self, path):
        self.__path = path
        return self

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

    def with_url(self, scheme=None, netloc=None, path=None):
        self.__url = build_url(scheme, netloc, path)
        return self

    def with_headers(self, headers: dict):
        self._session = self._session.with_headers(headers)
        return self
