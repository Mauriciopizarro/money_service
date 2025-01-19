from fastapi import APIRouter, Depends, HTTPException
from dependency_injector.wiring import inject, Provide
from infrastructure.injector import Injector
from domain.exceptions.exceptions import WalletAlreadyCreated

router = APIRouter()


@router.post("/wallet/create_wallet/{user_id}")
@inject
async def create_wallet(user_id, create_wallet_service=Depends(Provide[Injector.create_wallet_service])):
    try:
        return create_wallet_service.create_wallet(user_id).dict()
    except WalletAlreadyCreated:
        raise HTTPException(
            status_code=400, detail="Wallet already created",
        )
