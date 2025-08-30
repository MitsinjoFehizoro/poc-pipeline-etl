from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    url: str
    db_user: str
    db_password: str

    categories_table: str
    products_table: str
    payment_methods_table: str
    sales_table: str

    @property
    def properties(self) -> dict:
        return {
            "user": self.db_user,
            "password": self.db_password,
            "driver": "org.postgresql.Driver",
        }

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()
