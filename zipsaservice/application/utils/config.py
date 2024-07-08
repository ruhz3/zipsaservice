from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', 
        env_file_encoding='utf-8', 
        env_ignore_empty=True, 
        extra='ignore'
    )

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DBNAME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_POOL_MIN_SIZE: int
    POSTGRES_POOL_MAX_SIZE: int

    CRYPT_ALGORITHM: str
    HASH_ALGORITHM: str
    TOKEN_EXPIRE_TIMEDELTA: int

    ZIPSA_API_HOST: str
    ZIPSA_API_PORT: int
    