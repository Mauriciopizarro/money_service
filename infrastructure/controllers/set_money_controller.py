from fastapi import APIRouter
from typing import Union
from pydantic import BaseModel, confloat
from application.set_money_service import SetMoneyService

router = APIRouter()
set_money_service = SetMoneyService()


class SetMoneyRequestData(BaseModel):
    user_id: Union[int, str]
    amount: confloat(gt=-1)


@router.post("/wallet/set_money")
async def set_money_controller(request: SetMoneyRequestData):
    return set_money_service.set_money(request.user_id, request.amount)

