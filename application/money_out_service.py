from dependency_injector.wiring import inject, Provide
from domain.exceptions.exceptions import InsufficientFundsException, NotWalletFound
from infrastructure.injector import Injector
from domain.interfaces.wallet_repository import WalletRepository
from fastapi import HTTPException


class MoneyOutService:

    @inject
    def __init__(self, wallet_repository: WalletRepository = Provide[Injector.wallet_repo]):
        self.wallet_repository = wallet_repository

    def out_money(self, user_id, amount):
        try:
            wallet = self.wallet_repository.get_by_user_id(user_id)
            wallet.extract_money(amount)
            self.wallet_repository.update(wallet)
        except InsufficientFundsException:
            raise HTTPException(
                status_code=400, detail='Insufficient funds',
            )
        except NotWalletFound:
            raise HTTPException(
                status_code=400, detail='Wallet not found for this user',
            )
