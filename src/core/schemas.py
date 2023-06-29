import re

# from pydantic import EmailStr, Field, validator

from src.models import ORJSONModel


class WithdrawData(ORJSONModel):
    order_id: int
    wallet_address: str
    amount: float
    crypto_code: str
    signature: str
    
     
class WithdrawResponse(ORJSONModel):
    result: str
    data: dict
    