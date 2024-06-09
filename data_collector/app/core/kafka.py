import json

from functools import lru_cache
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer

from app.core.config import settings


class KafkaProducer:
    def __init__(self, bootstrap_servers: str):
        self.bootstrap_servers = bootstrap_servers
        self.producer = None

    async def __aenter__(self):
        self.producer = AIOKafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        await self.producer.start()
        return self.producer

    async def __aexit__(self, exc_type, exc, tb):
        if self.producer:
            await self.producer.stop()


class KafkaConsumer:
    def __init__(self, bootstrap_servers: str, topic: str):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.consumer = None

    async def __aenter__(self):
        self.consumer = AIOKafkaConsumer(self.topic, bootstrap_servers=self.bootstrap_servers)
        await self.consumer.start()
        return self.consumer

    async def __aexit__(self, exc_type, exc, tb):
        if self.consumer:
            await self.consumer.stop()


@lru_cache()
def get_kafka_consumer(topic: str = settings.KAFKA_TOPIC) -> KafkaConsumer:
    return KafkaConsumer(bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS, topic=topic)


@lru_cache()
def get_kafka_producer() -> KafkaProducer:
    return KafkaProducer(bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS)
