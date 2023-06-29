import typing

import sha3
from typing import Any
from src.core.config import executor_config
from src.core.schemas import WithdrawData
from src.core.exceptions import InvalidSignature
from ecdsa import VerifyingKey
def get_min_approve(amount):
    for conf in executor_config.LIMIT_AMOUNT:
        _limit = conf.get('limit')
        if isinstance(conf.get('limit'), tuple):
            if _limit[0] <= amount < _limit[1]:
                return conf.get('node')
    return 0


def verify(data: typing.Dict):
    signatures = data.get('signatures')

    del data['signatures']
    def _verify(node: int):
        pub_key = executor_config.PUBLIC_KEYS[node]

        _sig = signatures[node]

        _msg = {**data, 'node': node}

        _keys = list(_msg.keys())
        _keys.sort()
        _value = [str(_msg[i]) for i in _keys]
        _hash = sha3.keccak_256()
        for _item in _value:
            _hash.update(bytes(str(_item), 'utf-8'))

        _message = bytes(_hash.hexdigest(), 'utf-8')
        _pub = VerifyingKey.from_pem(pub_key)
        return _pub.verify(bytes.fromhex(_sig), _message)

    _min = get_min_approve(float(data['quantity']))
    print("get_min_approve", _min)

    if _min == 0 or len(signatures.keys()) < _min:
        print("Not enough approve")
        return False

    for _node in executor_config.PUBLIC_KEYS.keys():
        if not _verify(_node):
            print("Verify failed", _node)
            return False
    print("Pass verify")
    return True

def verify_withdrawal_signatures(withdrawal_data: WithdrawData) -> bool:
    try:
        if not verify(withdrawal_data.dict()):
            raise InvalidSignature()
    except:
        raise InvalidSignature()
