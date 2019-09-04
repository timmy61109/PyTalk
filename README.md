Talk
===
利用Python撰寫的點對點或中央談話程式，可以選擇使用不同的加密演算法保護傳輸的資料。
Peer-to-peer or central talk program written in Python.

使用Python3.6，並且使用以下套件:
- fastecdsa
- pycryptodome
- socket

支援的加密演算法:
- 「對稱性加密演算法」(Symmetric ciphers)
    - 「串流加密法」(Stream ciphers)
      - ciphers
        - ChaCha20
        - XChaCha20
        - Salsa20
      - authentication (MAC)
        - Poly1305
    - 「區塊加密法」(Block ciphers)
      - Ciphers
        - AES
      - Classic modes of operation
        - ECB mode
        - CBC mode
        - CTR mode
        - CFB mode
        - OFB mode
        - OpenPGP mode
      - Modern modes of operation
        - CCM mode
        - EAX mode
        - GCM mode
        - SIV mode
        - OCB mode

- 「非對稱性加密演算法」(Asymmetric ciphers):
  - RSA
  - ECC

- Hybrid ciphers:結合兩者
