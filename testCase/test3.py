import requests
import time
from common.createsign import CreatSign
import json
import unittest


class TerminalDetail(unittest.TestCase):
    def test_query(self):
        test = CreatSign()
        url = 'http://api.ext.m-m10010.com/open/unicom/TerminalDetail'
        headers = {'Content-Type': 'application/json'}
        params1 = {"userId": "131415929",
                   "num": "89860616020062438549",
                   "num_type": "iccid",
                   "timestamp": int(time.time()),
                   "sign": test.getsign()}
        response = requests.post(url, json=params1, headers=headers, verify=False)
        print(response.json()["error"])
        self.assertTrue('已激活' in response.text)
        self.assertIn('已激活', response.text)
        #self.assertEqual('success', result, msg="失败的时候，打印这里")


if __name__ == '__main__':
    unittest.main()

