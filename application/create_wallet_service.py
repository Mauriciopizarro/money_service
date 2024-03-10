from domain.Wallet import Wallet
from domain.interfaces.wallet_repository import WalletRepository
from dependency_injector.wiring import inject, Provide
from infrastructure.injector import Injector
from domain.exceptions.exceptions import WalletAlreadyCreated


class CreateWalletService:

    @inject
    def __init__(self, wallet_repository: WalletRepository = Provide[Injector.wallet_repo]):
        self.wallet_repository = wallet_repository

    def create_wallet(self, user_id):
        if self.wallet_repository.check_new_wallet_created(user_id):
            raise WalletAlreadyCreated()
        wallet = Wallet(amount=0, user_id=user_id)
        return self.wallet_repository.save(wallet)
