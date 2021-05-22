import subprocess
import urllib.request
import os
import ssl

if not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
    ssl._create_default_https_context = ssl._create_unverified_context

# c:\dev\envs\wnapi_env\Scripts\generateDS.exe
# /home/mf/envs/wnapi2/bin/generateDS
gds_args = '--use-getter-setter=new --no-dates --no-versions -f -o'
gds_template = '%s --user-methods=rest_user_methods --export="etree literal" %s %s %s'

base_host = 'https://vagrant.wntps.com'
# base_host = 'http://wn:8080'

gateway_xsd = 'gateway.xsd'
rest_xsd = 'rest.xsd'
boarding_xsd = 'boarding.xsd'
paylink_xsd = 'paylink.xsd'
payment_page_xsd = 'payment_page.xsd'

gateway_url = base_host + '/merchant/' + gateway_xsd
paylink_url = base_host + '/merchant/' + paylink_xsd
rest_url = base_host + '/merchant/terminal/application.wadl/xsd0.xsd'

gateway_args = ["generateDS", "--user-methods", "gateway_user_methods", "--export", "etree literal",
                "--use-getter-setter", "new", "--no-dates", "--no-versions", "-f", "-o", "gateway.py", gateway_xsd]
rest_args = ["generateDS", "--user-methods", "rest_user_methods", "--export", "etree literal", "--use-getter-setter",
             "new", "--no-dates", "--no-versions", "-f", "-o", "rest.py", rest_xsd]
paylink_args = ["generateDS", "--user-methods", "paylink_user_methods", "--export", "etree literal",
                "--use-getter-setter", "new", "--no-dates", "--no-versions", "-f", "-o", "paylink.py", paylink_xsd]
payment_page_args = ["generateDS", "--user-methods", "boarding_user_methods", "--export", "etree literal",
                     "--use-getter-setter", "new", "--no-dates", "--no-versions", "-f", "-o", "payment_page.py",
                     payment_page_xsd]
for r in [(gateway_url, gateway_xsd), (rest_url, rest_xsd), (paylink_url, paylink_xsd)]:
    response = urllib.request.urlretrieve(r[0], r[1])

with open(rest_xsd) as f:
    n = f.read().replace('e="50"', 'e="A50"').replace('5F20', 'A5F20').replace('9F26', 'A9F26').replace('9F06', 'A9F06')
with open(rest_xsd, "w") as f:
    f.write(n)

subprocess.Popen(gateway_args, stdout=subprocess.PIPE)
subprocess.Popen(rest_args, stdout=subprocess.PIPE)
subprocess.Popen(paylink_args, stdout=subprocess.PIPE)
subprocess.Popen(payment_page_args, stdout=subprocess.PIPE)
