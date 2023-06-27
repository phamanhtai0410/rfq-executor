import hashlib
from ecdsa import SigningKey, VerifyingKey
import sha3


# _private_key = SigningKey.generate()
# _public_key = _private_key.verifying_key
# print("* Private Key = ", _private_key.to_pem())
# print("* Public Key = ", _public_key.to_pem())

# with open("key/private.pem", "wb") as f:
#     f.write(_private_key.to_pem())
    
# with open("key/public.pem", "wb") as f:
#     f.write(_public_key.to_pem())


_private_key = '''-----BEGIN EC PRIVATE KEY-----
MF8CAQEEGNRRT0H13HIRxs8pBiTkJVVdQLzcIIKgiKAKBggqhkjOPQMBAaE0AzIA
BG+EQ6fFWWYeOpzvL70fPmEPC6fLNeHciP+v32oU50tlImSU1vGpFsm/tLpOVtxq
2A==
-----END EC PRIVATE KEY-----'''

_pub_key = '''-----BEGIN PUBLIC KEY-----
MEkwEwYHKoZIzj0CAQYIKoZIzj0DAQEDMgAEb4RDp8VZZh46nO8vvR8+YQ8Lp8s1
4dyI/6/fahTnS2UiZJTW8akWyb+0uk5W3GrY
-----END PUBLIC KEY-----'''

_private = SigningKey.from_pem(_private_key)
_pub = VerifyingKey.from_pem(_pub_key)

_data = [
    1,
    "0x29E754233F6A50ee5AE3ee6A0217aD907dc3386B",
    0.01,
    "ETH_TEST3"
]

_hash = sha3.keccak_256()
for _item in _data:
    _hash.update(bytes(str(_item),'utf-8'))
    
print("* Hash string = ", _hash.hexdigest())

_message = bytes(_hash.hexdigest(), 'utf-8')

_sig = _private.sign(_message)
print("=> Signature : ", _sig.hex())

_pub.verify(bytes.fromhex(_sig.hex()), _message)
print("=> Done verify sig => Valid Signature")