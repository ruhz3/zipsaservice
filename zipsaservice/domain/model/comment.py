from pydantic import BaseModel


class Comment(BaseModel):
    id: str
    post_id: str
    