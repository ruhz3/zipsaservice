from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str
    phone: str
    email: str
    address: Optional[str]
