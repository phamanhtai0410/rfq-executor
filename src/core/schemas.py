import re

# from pydantic import EmailStr, Field, validator

from src.models import ORJSONModel


class WithdrawData(ORJSONModel):
    transaction_id: str
    quantity: str
    currency: str
    wallet: str
    withdraw_uuid: str
    signatures: dict
    
     
class WithdrawResponse(ORJSONModel):
    result: str
    data: dict
    