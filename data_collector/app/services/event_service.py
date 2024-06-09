from functools import lru_cache

from fastapi import Depends

from app.core.kafka import get_kafka_producer, KafkaProducer
from app.core.config import settings
from app.schemas.event import Event


class EventService:

    def __init__(self, producer: KafkaProducer) -> None:
        self.producer = producer

    async def save_event(self, event: Event) -> None:
        async with self.producer as producer:
            await producer.send_and_wait(topic=settings.KAFKA_TOPIC, value=event.dict())


@lru_cache()
def get_event_service(producer: KafkaProducer = Depends(get_kafka_producer)) -> EventService:
    return EventService(producer=producer)
