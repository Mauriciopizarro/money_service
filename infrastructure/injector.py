from dependency_injector import containers, providers
from application.create_wallet_service import CreateWalletService
from application.get_wallet_service import GetWalletService
from application.money_out_service import MoneyOutService
from application.set_money_service import SetMoneyService
from infrastructure.repositories.wallet_mongo_repository import WalletMongoRepository


class Injector(containers.DeclarativeContainer):

    wallet_repo = providers.Singleton(WalletMongoRepository)
    get_wallet_service = providers.Factory(GetWalletService, wallet_repository=wallet_repo)
    money_out_service = providers.Factory(MoneyOutService, wallet_repository=wallet_repo)
    create_wallet_service = providers.Factory(CreateWalletService, wallet_repository=wallet_repo)
    set_money_service = providers.Factory(SetMoneyService, wallet_repository=wallet_repo)

    wiring_config = containers.WiringConfiguration(modules=[
        "infrastructure.controllers.get_wallet_controller",
        "infrastructure.controllers.money_out_controller",
        "infrastructure.controllers.save_wallet_controller",
        "infrastructure.controllers.set_money_controller"
    ])
