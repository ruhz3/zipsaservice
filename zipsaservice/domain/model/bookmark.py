from pydantic import BaseModel


class Bookmark(BaseModel):
    id: str
    account_id: str
    house_id: int
