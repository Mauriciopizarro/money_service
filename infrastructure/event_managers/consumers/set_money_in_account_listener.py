import json
from infrastructure.event_managers.rabbit_consumer import RabbitConsumer
from logging.config import dictConfig
import logging
import requests
from infrastructure.logging import LogConfig

dictConfig(LogConfig().dict())
logger = logging.getLogger("blackjack")


class SetMoneyAccountListener(RabbitConsumer):
    topic = "set_money_account"

    def process_message(self, channel, method, properties, body):
        logger.info('Received message')
        event = json.loads(body)
        user_id = event["user_id"]
        amount = event["amount"]
        url = "http://money_service:5003/wallet/set_money"
        requests.post(url=url, json={
            "user_id": user_id,
            "amount": amount
        })
        logger.info('Message consumed')
