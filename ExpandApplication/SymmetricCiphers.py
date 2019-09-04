import json
from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes


class stream_ciphers():
    def __init__(self, key=None, encrypt_method="aes-256-cfb", iv=None,
                 segment_size=8, nonce=None, initial_value=None,
                 counter=None):
        self.__key = key
        self.__encrypt_method = encrypt_method
        self.__iv = iv
        self.__segment_size = segment_size
        self.__nonce = nonce
        self.__initial_value = initial_value
        self.__counter = counter
        self.__items = None

    def encrypt(self, message="test"):
        """aaa."""
        cipher, iv, segment_size, nonce, initial_value, counter = next(
            self.encrypt_method)
        message = message.encode('utf8')
        if self.__items[2] == "cfb":
            ct_bytes = cipher.encrypt(pad(message, AES.block_size))
        else:
            ct_bytes = cipher.encrypt(message)

        ct_b64 = b64encode(ct_bytes).decode('utf-8')

        result = {
            'iv': self.__iv,
            'segment_size': self.__segment_size,
            'nonce': self.__nonce,
            'initial_value': self.__initial_value,
            'counter': self.__counter,
            'ciphertext': ct_b64,
        }

        result = json.dumps(result)
        yield result.encode('utf8')

    def decrypt(self, cipher_message):
        # We assume that the key was securely shared beforehand
        try:
            cipher_message = cipher_message.encode('utf8')
            b64 = json.loads(cipher_message)

            iv = b64decode(b64['iv'])
            segment_size = b64decode(b64['segment_size'])
            nonce = b64decode(b64['nonce'])
            initial_value = b64decode(b64['initial_value'])
            counter = b64decode(b64['counter'])
            ct = b64decode(b64['ciphertext'])

            self.reset_encrypt_method(
                key=self.__key,
                encrypt_method=self.__encrypt_method,
                iv=iv,
                segment_size=segment_size,
                nonce=nonce,
                initial_value=initial_value,
                counter=counter
                )

            cipher, iv, segment_size, nonce, initial_value, counter = next(
                self.encrypt_method)

            if self.__items[2] == "cfb":
                pt = unpad(cipher.decrypt(ct), AES.block_size)
            else:
                pt = cipher.decrypt(ct)

            yield pt

        except:
            print("Incorrect decryption")

    @property
    def encrypt_method(self):
        if self.__key is None:
            self.__key = get_random_bytes(16)
        else:
            self.__key = self.__key

        if len(self.__key) % 8 != 0:
            raise ValueError('金鑰長度必須是符合8的倍數')

        self.__items = items = self.__encrypt_method.split("-")
        if items[1] == len(self.__key) * 16:
            raise ValueError('不符合金鑰設定的位元長度')

        if items[0] == "aes":
            if items[2] == "ecb":
                cipher = AES.new(self.__key, AES.MODE_ECB)

            elif items[2] == "cbc":
                cipher = AES.new(self.__key, AES.MODE_CBC, iv=self.__iv)
                self.__iv = b64encode(cipher.iv).decode('utf-8')

            elif items[2] == "ctr":
                cipher = AES.new(self.__key, AES.MODE_CTR, nonce=self.__nonce,
                                 initial_value=self.__initial_value,
                                 counter=self.__counter)
                self.__nonce = b64encode(cipher.nonce).decode('utf-8')

            elif items[2] == "cfb":
                cipher = AES.new(self.__key, AES.MODE_CFB, iv=self.__iv,
                                 segment_size=self.__segment_size)
                self.__iv = b64encode(cipher.iv).decode('utf-8')

            elif items[2] == "ofb":
                cipher = AES.new(self.__key, AES.MODE_OFB, iv=self.__iv)
                self.__iv = b64encode(cipher.iv).decode('utf-8')

            elif items[2] == "openpgp":
                cipher = AES.new(self.__key, AES.MODE_OPENPGP)

            else:
                raise ValueError('沒有此加密演算法')

        else:
            raise ValueError('沒有此加密演算法')

        iv = self.__iv
        segment_size = self.__segment_size
        nonce = self.__nonce
        initial_value = self.__initial_value
        counter = self.__counter
        yield cipher, iv, segment_size, nonce, initial_value, counter

    def reset_encrypt_method(self, key=None, encrypt_method="aes-256-cfb",
                             iv=None, segment_size=None, nonce=None,
                             initial_value=None, counter=None):
        self.__key = key
        self.__encrypt_method = encrypt_method
        self.__iv = iv
        self.__segment_size = segment_size
        self.__nonce = nonce
        self.__initial_value = initial_value
        self.__counter = counter


sc = stream_ciphers()
print(next(sc.encrypt()))
print(next(sc.encrypt()))
