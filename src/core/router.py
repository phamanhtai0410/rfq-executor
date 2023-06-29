from databases.interfaces import Record
from fastapi import APIRouter, BackgroundTasks, Depends, Response, status
from src.core.utils import verify_withdrawal_signatures
from src.core import service
from src.core.dependencies import (
    valid_withdraw_data
)
from src.core.schemas import WithdrawResponse, WithdrawData

router = APIRouter()

@router.post("/withdraw", response_model=WithdrawResponse)
async def withdraw(
    worker: BackgroundTasks,
    withdraw_data: WithdrawData = Depends(valid_withdraw_data)
) -> WithdrawResponse:
    # Verify the signature
    verify_withdrawal_signatures(withdrawal_data=withdraw_data)
    
    print("- Withdraw action with data ", withdraw_data)
    
    worker.add_task(
        service.withdraw_to_address,
       withdraw_data
    )
    return WithdrawResponse(
        result="Executed the withdrawal",
        data={}
        # _tx if _tx else {
        #     "Exception": "Error when execute the withdrawal"
        # }
    )