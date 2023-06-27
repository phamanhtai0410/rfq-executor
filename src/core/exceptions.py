from src.core.constants import ErrorCode
from src.exceptions import BadRequest, NotAuthenticated, PermissionDenied


    
class InvalidWithdrawalAddress(BadRequest):
    DETAIL = ErrorCode.INVALID_WITHDRAWAL_ADDRESS
    
class InvalidWithdrawalAssetCode(BadRequest):
    DETAIL = ErrorCode.INVALID_ASSET_CODE
    
class InvalidSignature(BadRequest):
    DETAIL = ErrorCode.INVALID_SIGNATURE

class InvalidOrderId(BadRequest):
    DETAIL = ErrorCode.INVALID_ORDER_ID