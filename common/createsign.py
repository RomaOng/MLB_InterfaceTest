import Crypto
import time
import hashlib
import string


class CreatSign():

    def getsign(self):
        id = "131415929"
        key = "379C68321D4C3FD90E139A2EB982189E"
        timestamp = int(time.time())
        str1 = id + key + str(timestamp)
        md5_key = hashlib.md5()
        md5_key.update(str1.encode())
        sign = md5_key.hexdigest().upper()
        return sign
