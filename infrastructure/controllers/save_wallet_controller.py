from fastapi import APIRouter
from application.create_wallet_service import CreateWalletService
from fastapi import HTTPException
from domain.exceptions.exceptions import WalletAlreadyCreated

router = APIRouter()
create_wallet_service = CreateWalletService()


@router.post("/wallet/create_wallet/{user_id}")
async def create_wallet(user_id):
    try:
        return create_wallet_service.create_wallet(user_id).dict()
    except WalletAlreadyCreated:
        raise HTTPException(
            status_code=400, detail="Wallet already created",
        )
