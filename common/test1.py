import requests
import time
from createsign import CreatSign
import json

test = CreatSign()
url = 'http://api.ext.m-m10010.com/open/unicom/TerminalDetail'
headers = {'Content-Type': 'application/json'}
params1 = {"userId": "131415929",
           "num": "89860616020062438549",
           "num_type": "iccid",
           "timestamp": int(time.time()),
           "sign": test.getsign()}

response = requests.post(url, json=params1, headers=headers, verify=False)
print(response.json())
print(response.status_code)
print(response.json().get('error'))

if response.status_code == 200 and response.json().get('error') == 0:
    print("用例通过")
else:
    print("用例不通过")
