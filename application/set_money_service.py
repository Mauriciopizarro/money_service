from domain.exceptions.exceptions import InvalidIncomeAmountException
from domain.interfaces.wallet_repository import WalletRepository


class SetMoneyService:

    def __init__(self, wallet_repository: WalletRepository):
        self.wallet_repository = wallet_repository

    def set_money(self, user_id, amount):
        if amount < 1:
            raise InvalidIncomeAmountException()
        wallet = self.wallet_repository.get_by_user_id(user_id)
        wallet.set_money(amount)
        self.wallet_repository.update(wallet)
        return wallet.dict()
