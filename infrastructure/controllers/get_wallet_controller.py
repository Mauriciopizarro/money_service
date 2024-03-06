from fastapi import APIRouter, Depends, HTTPException
from application.get_wallet_service import GetWalletService
from domain.Wallet import Wallet
from domain.exceptions.exceptions import IncorrectUserID

router = APIRouter()
get_wallet_service = GetWalletService()


@router.get("/wallet/get/{user_id}", response_model=Wallet)
async def get_wallet(user_id):
    try:
        wallet = get_wallet_service.wallet_by_user(user_id)
        return wallet.dict()
    except IncorrectUserID:
        raise HTTPException(
            status_code=404, detail='Wallet for this user not found',
        )
