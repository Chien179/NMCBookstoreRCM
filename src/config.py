from pydantic_settings import BaseSettings


class Config(BaseSettings):
    class Config:
        env_file = ".env"

    POSTGRES_URI: str
    PORT: int


config = Config()
