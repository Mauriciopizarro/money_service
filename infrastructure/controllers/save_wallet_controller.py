from fastapi import APIRouter
from application.create_wallet_service import CreateWalletService

router = APIRouter()
create_wallet_service = CreateWalletService()


@router.post("/wallet/create_wallet/{user_id}")
async def create_wallet(user_id):
    return create_wallet_service.create_wallet(user_id).dict()
