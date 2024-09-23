from pydantic import BaseModel, EmailStr, PositiveInt, PastDatetime, ConfigDict
from typing import Union


class SArticleAdd(BaseModel):
    title: str
    text: str
    author: Union[str, None] = None
    source: Union[str, None] = None


class SArticle(SArticleAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)
