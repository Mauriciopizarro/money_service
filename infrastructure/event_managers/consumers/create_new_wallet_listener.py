import json
from infrastructure.event_managers.rabbit_consumer import RabbitConsumer
from logging.config import dictConfig
import logging
import requests
from infrastructure.logging import LogConfig

dictConfig(LogConfig().dict())
logger = logging.getLogger("blackjack")


class CreateNewWalletListener(RabbitConsumer):
    topic = "create_new_wallet"

    def process_message(self, channel, method, properties, body):
        logger.info('Received message')
        event = json.loads(body)
        user_id = event["user_id"]
        url = f"http://money_service:5003/wallet/create_wallet/{user_id}"
        requests.post(url=url)
        logger.info('Message consumed')
