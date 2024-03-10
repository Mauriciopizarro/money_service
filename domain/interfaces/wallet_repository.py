from abc import ABC, abstractmethod
from domain.Wallet import Wallet


class WalletRepository(ABC):

    @abstractmethod
    def save(self, wallet: Wallet) -> Wallet:
        pass

    @abstractmethod
    def get(self, wallet_id) -> Wallet:
        pass

    @abstractmethod
    def get_by_user_id(self, user_id) -> Wallet:
        pass

    @abstractmethod
    def check_new_wallet_created(self, user_id):
        pass

    @abstractmethod
    def update(self, wallet: Wallet) -> Wallet:
        pass
