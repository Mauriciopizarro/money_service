from pydantic import BaseModel, confloat
from typing import Union
from domain.exceptions.exceptions import *


class Wallet(BaseModel):

    amount: confloat(gt=-1)
    user_id: Union[int, str]

    def set_money(self, amount: float):
        self.amount += amount

    def get_money(self) -> float:
        return self.amount

    def extract_money(self, amount_to_extract):
        if amount_to_extract > self.amount:
            raise InsufficientFundsException("Insufficient funds")
        self.amount -= amount_to_extract
