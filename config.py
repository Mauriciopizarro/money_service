from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_MONGO_URL: str
    RABBIT_USERNAME: str
    RABBIT_PASSWORD: str
    RABBIT_HOST: str
    RABBIT_VHOST: str

    class Config:
        env_file = './.env'


settings = Settings()
