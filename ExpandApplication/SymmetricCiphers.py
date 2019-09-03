import json
from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes


class stream_ciphers():
    def __init__(self, key=None, encrypt_method="aes-256-cfb", iv=None,
                 segment_size=None, nonce=None, initial_value=None,
                 counter=None):
        self.__key = key
        self.__encrypt_method = encrypt_method
        self.__iv = iv
        self.__segment_size = segment_size
        self.__nonce = nonce
        self.__initial_value = initial_value
        self.__counter = counter

    def encrypt(self, message=b'test'):
        cipher = self.mode
        ct_bytes = cipher.encrypt(pad(message, AES.block_size))
        iv = b64encode(cipher.iv).decode('utf-8')
        ct = b64encode(ct_bytes).decode('utf-8')
        result = json.dumps({'iv': iv, 'ciphertext': ct})
        yield result.encode('utf8')

    def decrypt(self):
        # We assume that the key was securely shared beforehand
        try:
            b64 = json.loads(json_input)
            iv = b64decode(b64['iv'])
            ct = b64decode(b64['ciphertext'])
            cipher = AES.new(key, AES.MODE_CBC, iv)
            pt = unpad(cipher.decrypt(ct), AES.block_size)
            print("The message was: ", pt)
        except:
            print("Incorrect decryption")

    @property
    def mode(self):
        if len(self.__key) % 8 == 0:
            raise ValueError('字元數必須是符合8的倍數')

        if self.__key is None:
            self.__key = get_random_bytes()
        else:
            self.__key = self.__key

        items = self.__encrypt_method.split("-")
        if items[1] == len(self.__key) * 16:
            raise ValueError('不符合金鑰設定的位元長度')

        if items[0] == "aes":
            if items[2] == "ecb":
                cipher = AES.new(self.__key, AES.MODE_ECB)

            elif items[2] == "cbc":
                cipher = AES.new(self.__key, AES.MODE_CBC)

            elif items[2] == "ctr":
                cipher = AES.new(self.__key, AES.MODE_CTR)

            elif items[2] == "cfb":
                cipher = AES.new(self.__key, AES.MODE_CFB)

            elif items[2] == "ofb":
                cipher = AES.new(self.__key, AES.MODE_OFB)

            elif items[2] == "openpgp":
                cipher = AES.new(self.__key, AES.MODE_OPENPGP)

            else:
                raise ValueError('沒有此加密演算法')

        else:
            raise ValueError('沒有此加密演算法')

    @mode.setter
    def mode(self, radius):
        self.__radius = radius
