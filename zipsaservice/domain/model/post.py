from typing import Literal
from pydantic import BaseModel
from zipsaservice.domain.model.user import User


class Post(BaseModel):
    writer: User
    content: str
    created_at: str
    updated_at: str


class Article(Post):
    id: str
    title: str
    type: Literal['notice', 'qna', 'post']


class Comment(Post):
    id: str
    