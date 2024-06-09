from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_SLUG: str = Field(title="Project slug", default="Data collector")
    API_V1_STR: str = Field(title="Base str", default="api/v1")

    KAFKA_BOOTSTRAP_SERVERS: str = Field(title="Kafka server")
    KAFKA_TOPIC: str = Field(title="Kafka topic")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
