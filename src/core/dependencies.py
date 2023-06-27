from datetime import datetime

from databases.interfaces import Record
from fastapi import Cookie, Depends
from web3 import Web3
from src.core import service
from src.core.exceptions import InvalidWithdrawalAddress
from src.core.schemas import WithdrawData


def valid_withdraw_data(withdraw_data: WithdrawData) -> bool:
    if not Web3.is_address(withdraw_data.wallet_address):
        raise InvalidWithdrawalAddress()
    return withdraw_data