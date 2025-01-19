from domain.interfaces.wallet_repository import WalletRepository


class GetWalletService:

    def __init__(self, wallet_repository: WalletRepository):
        self.wallet_repository = wallet_repository

    def wallet_by_user(self, user_id):
        return self.wallet_repository.get_by_user_id(user_id)
