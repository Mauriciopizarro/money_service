from domain.Wallet import Wallet
from domain.interfaces.wallet_repository import WalletRepository
from pymongo import MongoClient
from config import settings
from bson.objectid import ObjectId
from domain.exceptions.exceptions import *


class WalletMongoRepository(WalletRepository):
    instance = None

    def __init__(self):
        self.db = self.get_database()

    # singleton pattern
    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()

        return cls.instance

    @staticmethod
    def get_database():
        client = MongoClient(settings.DATABASE_MONGO_URL)
        return client['blackjack']["wallet"]

    def get(self, wallet_id) -> Wallet:
        if not ObjectId.is_valid(wallet_id):
            raise IncorrectObjectID()
        wallet_dict = self.db.find_one({"_id": ObjectId(wallet_id)})
        if not wallet_dict:
            raise IncorrectWalletID()
        return Wallet(amount=wallet_dict.get('amount'), user_id=wallet_dict.get('user_id'))

    def get_by_user_id(self, user_id) -> Wallet:
        wallet_dict = self.db.find_one({"user_id": user_id})
        if not wallet_dict:
            raise IncorrectUserID()
        return Wallet(amount=wallet_dict.get('amount'), user_id=user_id)

    def save(self, wallet: Wallet) -> Wallet:
        return Wallet(amount=wallet.amount, user_id=wallet.user_id)

    def update(self, wallet: Wallet) -> Wallet:
        wallet_dict = wallet.dict()
        self.db.find_one_and_update({"user_id": wallet.user_id}, {"$set": wallet_dict})
        return Wallet(amount=wallet.amount, user_id=wallet.user_id)
