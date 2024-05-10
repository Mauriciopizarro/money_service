from fastapi import APIRouter, HTTPException
from typing import Union
from pydantic import BaseModel, confloat
from application.set_money_service import SetMoneyService
from domain.exceptions.exceptions import NotWalletFound, InvalidIncomeAmountException

router = APIRouter()
set_money_service = SetMoneyService()


class SetMoneyRequestData(BaseModel):
    user_id: Union[int, str]
    amount: confloat(gt=-1)


@router.post("/wallet/set_money")
async def set_money_controller(request: SetMoneyRequestData):
    try:
        return set_money_service.set_money(request.user_id, request.amount)
    except NotWalletFound:
        raise HTTPException(
            status_code=404, detail='This user does not have a wallet',
        )
    except InvalidIncomeAmountException:
        raise HTTPException(
            status_code=404, detail='The income amount must be greater than 0',
        )
