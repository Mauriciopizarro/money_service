from fastapi import APIRouter
from typing import Union
from pydantic import BaseModel, confloat
from application.money_out_service import MoneyOutService

router = APIRouter()
money_out_service = MoneyOutService()


class MoneyOutRequestData(BaseModel):
    user_id: Union[int, str]
    amount: confloat(gt=-1)


@router.post("/wallet/money_out")
async def money_out_controller(request: MoneyOutRequestData):
    return money_out_service.out_money(request.user_id, request.amount)

