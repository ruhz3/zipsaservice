from pydantic import BaseModel
from zipsaservice.domain.model.user import User


class Account(BaseModel):
    id: str
    password: str
    user: User
    admin: bool = False
    