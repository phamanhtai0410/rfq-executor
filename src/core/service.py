import multiprocessing
from datetime import datetime, timedelta

from databases.interfaces import Record
from pydantic import UUID4
from src.core.schemas import WithdrawData
from fireblocks_sdk import FireblocksSDK, VAULT_ACCOUNT, TransferPeerPath, DestinationTransferPeerPath, ONE_TIME_ADDRESS
from src.core.config import executor_config
import requests
from src.core.exceptions import InvalidOrderId
from src.core.constants import Environments

last_withdraw_uuid = multiprocessing.Value('i', 0)
lock = multiprocessing.Lock()

async def update_withdrawal_result(
    data: dict
) -> None:
    _headers = {
        
    }
    _update = requests.post(
        url=executor_config.UPDATE_WITHDRAW_CALLBACK_URL,
        data=data,
        headers=_headers
    )
    return _update.text
    
def get_fireblock():
    api_secret = executor_config.FIREBLOCK_SECRET_KEY
    api_key = executor_config.FIREBLOCK_API_KEY
    api_url = executor_config.FIREBLOCK_API_URL
    return FireblocksSDK(api_secret, api_key, api_base_url=api_url)

async def create_transaction(asset_id, amount, src_id, address, note, external_tx_id) -> dict:
    fireblocks = get_fireblock()
    tx_result = fireblocks.create_transaction(
        asset_id=asset_id,
        amount=amount,
        source=TransferPeerPath(VAULT_ACCOUNT, src_id),
        destination=DestinationTransferPeerPath(ONE_TIME_ADDRESS, None, {"address": address}),
        note=note,
        external_tx_id=external_tx_id
    )
    print(tx_result)
    return tx_result

"""
    Function allow to withdraw one amount of token to wthdrawer
"""
async def withdraw_to_address(
    withdraw_data: WithdrawData,
    last_withdraw_uuid = last_withdraw_uuid,
    lock = lock
) -> dict:
    lock.acquire()
    print("Last id = ", last_withdraw_uuid.value)
    print("Current order id = ", withdraw_data.withdraw_uuid)
    
    # if last_withdraw_uuid.value >= withdraw_data.withdraw_uuid:
    #     lock.release()
    #     return {}
        # raise InvalidOrderId()
    
    last_withdraw_uuid.value = int(datetime.now().timestamp())
    print("* Withdraw Data = ", withdraw_data)
    
    _currency = withdraw_data.currency
    if executor_config.enviroment == Environments.STAGING:
        _currency = executor_config.mapping_crypto_code.get(withdraw_data.currency, _currency)
    
    # Make transfer tx in Fireblock
    _withdraw_tx = await create_transaction(
        asset_id=_currency,
        amount=str(withdraw_data.quantity),
        src_id=executor_config.WITHDRAWAL_POOL_ACCOUNT_ID,
        address=withdraw_data.wallet,
        note=f"Withdraw {withdraw_data.quantity} to address {withdraw_data.wallet}",
        external_tx_id=withdraw_data.withdraw_uuid
    )
    lock.release()
    # Update the withdrawal request
    # await update_withdrawal_result({
    #     "order_id": withdraw_data["order_id"],
    #     "fireblock_withdraw_id": _withdraw_tx["id"],
    #     "status": _withdraw_tx["status"]
    # })
    
    return _withdraw_tx
