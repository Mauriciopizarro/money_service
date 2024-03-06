from domain.interfaces.wallet_repository import WalletRepository
from dependency_injector.wiring import inject, Provide
from infrastructure.injector import Injector


class GetWalletService:

    @inject
    def __init__(self, wallet_repository: WalletRepository = Provide[Injector.wallet_repo]):
        self.wallet_repository = wallet_repository

    def wallet_by_user(self, user_id):
        return self.wallet_repository.get_by_user_id(user_id)
