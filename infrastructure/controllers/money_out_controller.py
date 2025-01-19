from fastapi import APIRouter, Depends, HTTPException
from typing import Union
from pydantic import BaseModel, confloat
from dependency_injector.wiring import inject, Provide
from infrastructure.injector import Injector
from domain.exceptions.exceptions import InsufficientFundsException, NotWalletFound

router = APIRouter()


class MoneyOutRequestData(BaseModel):
    user_id: Union[int, str]
    amount: confloat(gt=-1)


@router.post("/wallet/money_out")
@inject
async def money_out_controller(request: MoneyOutRequestData,
                               money_out_service=Depends(Provide[Injector.money_out_service])):
    try:
        return money_out_service.out_money(request.user_id, request.amount)
    except InsufficientFundsException:
        raise HTTPException(
            status_code=400, detail='Insufficient funds',
        )
    except NotWalletFound:
        raise HTTPException(
            status_code=400, detail='Wallet not found for this user',
        )
