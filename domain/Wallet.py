from pydantic import BaseModel, confloat
from typing import Union


class Wallet(BaseModel):

    amount: confloat(gt=-1)
    user_id: Union[int, str]

    def set_money(self, amount: float):
        self.amount += amount

    def get_money(self) -> float:
        return self.amount
