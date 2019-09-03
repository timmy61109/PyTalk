from fastecdsa import curve, ecdsa, keys
from fastecdsa.encoding.der import DEREncoder

message = "a message to sign via ECDSA"  # 一些訊息

print("使用預設曲線P256跟雜湊函數SHA2")
private_key = keys.gen_private_key(curve.P256)
public_key = keys.get_public_key(private_key, curve.P256)
print("私密金鑰: " + str(private_key))
print("公開金鑰: " + str(public_key))
print(type(public_key))

print("產生數位簽章，為兩個整數r跟s")
r, s = ecdsa.sign(message, private_key)
print(r)
print(s)

print("編碼數位簽章，使用DEREncoder為r跟s做編碼以利傳輸")
encoded = DEREncoder.encode_signature(r, s)
b = "數位簽章: "
for i in encoded:
    b += str(hex(i)) + " "
print(b)
decoded_r, decoded_s = DEREncoder.decode_signature(encoded)
valid = ecdsa.verify((decoded_r, decoded_s), message, public_key)
if r == decoded_r and s == decoded_s and valid:
    print("成功")
