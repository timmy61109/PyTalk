from fastecdsa import curve, ecdsa, keys
from fastecdsa.encoding.der import DEREncoder

message = "a message to sign via ECDSA"  # 一些訊息

"""
使用預設曲線跟雜湊函數(P256 and SHA2)
"""
private_key = keys.gen_private_key(curve.P256)
public_key = keys.get_public_key(private_key, curve.P256)
print(private_key)
print(public_key)
"""
產生數位簽章，為兩個整數r跟s。
"""
r, s = ecdsa.sign(message, private_key)
print(r)
print(s)
"""
編碼數位簽章，使用DEREncoder為r跟s做編碼以利傳輸
"""
encoded = DEREncoder.encode_signature(r, s)
print(encoded)
decoded_r, decoded_s = DEREncoder.decode_signature(encoded)
if r == decoded_r and s == decoded_s:
    decoded_r, decoded_s
    valid = ecdsa.verify((decoded_r, decoded_s), message, public_key)
    print(valid)
"""
valid應該返回True，驗證前面產生的私密金鑰(private_key)、公開金鑰(public_key)、
數位簽章(r, s)、加密訊息是有效的。
"""
public_key = b'X: 0x2b71ffb22f1e918e401f19c2ab4afa0fa9a4221c28c61cfde09dbbd28fb332b\nY: 0xdeb8a709e838a712156e3a5a8f189f4d1d1798de1f20417c5be65fc61606a384\n(On curve <P256>)'
valid = ecdsa.verify((decoded_r, decoded_s), message, public_key)
print(valid)
