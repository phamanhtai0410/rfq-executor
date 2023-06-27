import sha3
from typing import Any
from src.core.config import executor_config
from src.core.schemas import WithdrawData
from src.core.exceptions import InvalidSignature
from ecdsa import VerifyingKey

def verify_withdrawal_signature(withdrawal_data: WithdrawData) -> bool:
    try:    
        _data = [
            withdrawal_data.order_id,
            withdrawal_data.wallet_address,
            withdrawal_data.amount,
            withdrawal_data.crypto_code
        ]
        _hash = sha3.keccak_256()
        for _item in _data:
            _hash.update(bytes(str(_item),'utf-8'))
        _hash_string = bytes(_hash.hexdigest(), 'utf-8')
        _signature = bytes.fromhex(withdrawal_data.signature)
        _verifying_key = VerifyingKey.from_pem(executor_config.SIGNATURE_PUBKEY)
        _verifying_key.verify(_signature, _hash_string)
    except:
        raise InvalidSignature()
    