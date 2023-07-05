from ecdsa import SigningKey, VerifyingKey
import sha3
import json 


_private_key = '''-----BEGIN EC PRIVATE KEY-----
MF8CAQEEGNRRT0H13HIRxs8pBiTkJVVdQLzcIIKgiKAKBggqhkjOPQMBAaE0AzIA
BG+EQ6fFWWYeOpzvL70fPmEPC6fLNeHciP+v32oU50tlImSU1vGpFsm/tLpOVtxq
2A==
-----END EC PRIVATE KEY-----'''

_private = SigningKey.from_pem(_private_key)

_data = json.load(open('sign_for_executor/withdrawal_info.txt', 'r'))
print("* Data = ", _data)

_hash = sha3.keccak_256()
for _item in _data:
    _hash.update(bytes(str(_item),'utf-8'))
    
print("* Hash string = ", _hash.hexdigest())

_message = bytes(_hash.hexdigest(), 'utf-8')

_sig = _private.sign(_message)
print("=> Signature : ", _sig.hex())

# [
#     "BTC_TEST",
#     "USDT_T",
#     "USDC_T",
#     "AVAXTEST",
#     "SOL_TEST",
#     "LOOKS",
#     "APE",
#     "ETH_TEST",
#     "ETH_TEST1",
#     "ETH_TEST2",
#     "ETH_TEST3",
#     "ETH_TEST4",
#     "ETH_TEST5",
#     "DOT",
#     "EOS",
#     "ETC_TEST",
#     "GMT",
#     "LTC_TEST",
#     "MANA",
#     "NEAR_TEST",
#     "TRX_TEST",
#     "WAVES",
#     "FTT",
#     "FTM",
#     "MATIC_TEST",
#     "XLM",
#     "XRP",
#     "SAND",
#     "DOGE_TEST",
#     "CRV",
#     "BNB_TEST",
#     "ADA_TEST",
#     "AXS",
#     "USDT_BSC_TEST"
# ]
