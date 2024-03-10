from dependency_injector import containers, providers
from infrastructure.repositories.wallet_mongo_repository import WalletMongoRepository


class Injector(containers.DeclarativeContainer):

    wallet_repo = providers.Singleton(WalletMongoRepository)


injector = Injector()
injector.wire(modules=["application.get_wallet_service",
                       "application.create_wallet_service",
                       "application.set_money_service",
                       "application.money_out_service"
                       ])
