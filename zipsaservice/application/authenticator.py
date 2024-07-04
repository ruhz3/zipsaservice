from datetime import datetime, timedelta, timezone
from typing import Any
import secrets

from passlib.context import CryptContext
import jwt


class Authenticator:
    
    def __init__(
        self,
        crypt_algorithm: str,
        hash_algorithm: str,
        token_expire_min: int
    ) -> None:
        self._pwd_context = CryptContext(schemes=[crypt_algorithm], deprecated="auto")
        self._hash_algorithm = hash_algorithm
        self._token_expire_timedelta = timedelta(token_expire_min)
        self.__secret_key = secrets.token_urlsafe(32)
        
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self._pwd_context.verify(plain_password, hashed_password)
    
    def get_hashed(self, plain_password: str) -> str:
        return self._pwd_context.hash(plain_password)
    
    def create_access_token(self, subject: str | Any) -> str:
        expire = datetime.now(timezone.utc) + self._token_expire_timedelta
        to_encode = {"exp": expire, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, self.__secret_key, algorithm=self._hash_algorithm)
        return encoded_jwt
    