from pydantic import BaseModel, Field


class Event(BaseModel):
    user_id: str = Field(title="ID пользователя")
    event_type: str = Field(title="Тип события")
    timestamp: int = Field(title="Время события")
    metadata: dict = Field(title="Информация о событии")


class Message(BaseModel):
    message: str = Field(title="Сообщение об отправке")
