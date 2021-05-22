import json
import os

import pyotp

root_dir = os.path.dirname(os.path.abspath(__file__))
access_file_path = os.path.join(root_dir, "../credentials.json")

with open(access_file_path, "r") as json_file:
    data = json.load(json_file)

vpn = data['vpn']
current = vpn.get('vpn_name')
p = pyotp.totp.TOTP(current.get('key'))
print(current.get('pw') + p.now())
