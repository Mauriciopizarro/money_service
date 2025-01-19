from fastapi import APIRouter, Depends, HTTPException
from domain.Wallet import Wallet
from domain.exceptions.exceptions import NotWalletFound
from dependency_injector.wiring import inject, Provide
from infrastructure.injector import Injector

router = APIRouter()


@router.get("/wallet/get/{user_id}", response_model=Wallet)
@inject
async def get_wallet(user_id, get_wallet_service = Depends(Provide[Injector.get_wallet_service])):
    try:
        wallet = get_wallet_service.wallet_by_user(user_id)
        return wallet.dict()
    except NotWalletFound:
        raise HTTPException(
            status_code=404, detail='Wallet for this user not found',
        )
