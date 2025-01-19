from domain.interfaces.wallet_repository import WalletRepository


class MoneyOutService:

    def __init__(self, wallet_repository: WalletRepository):
        self.wallet_repository = wallet_repository

    def out_money(self, user_id, amount):
        wallet = self.wallet_repository.get_by_user_id(user_id)
        wallet.extract_money(amount)
        self.wallet_repository.update(wallet)

