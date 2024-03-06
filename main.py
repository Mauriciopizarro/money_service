from fastapi import FastAPI
from infrastructure.injector import Injector
from infrastructure.controllers import get_wallet_controller, save_wallet_controller, \
    set_money_controller

app = FastAPI()

app.include_router(get_wallet_controller.router)
app.include_router(save_wallet_controller.router)
app.include_router(set_money_controller.router)
