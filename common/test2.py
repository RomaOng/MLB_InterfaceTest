import requests
from configExcel import Excel
import time
from createsign import CreatSign

getexcel = Excel("F:/MLB_InterfaceTest/testFile/IMEI号导入格式 (1).xls", 0)
getsign1 = CreatSign()
num = []
i = getexcel.get_data().nrows
for j in range(0, i):
    num.append(getexcel.get_value(j, 0))

url = "http://api.ext.m-m10010.com/open/unicom/BatchQueryTerminal"
headers = {'Content-Type': 'application/json'}
params1 = {
    "userId": "131415929",
    "num": num,
    "num_type": "iccid",
    "timestamp": int(time.time()),
    "sign": getsign1.getsign()}
response = requests.post(url, json=params1, headers=headers, verify=False)
print(response.json())
print("\t")
print(response.json().get("result")[0].get("packagesn"))

if response.status_code == 200 and response.json().get('error') == 0:
    print("用例通过")
else:
    print("用例不通过")
