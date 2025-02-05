from pydantic import BaseModel


class JsonPlaceholderApiResponsePostModel(BaseModel):
    userId: int
    id: int
    title: str
    body: str


class JsonPlaceholderApiResponseAlbumModel(BaseModel):
    userId: int
    id: int
    title: str


class JsonPlaceholderApiRequestCommentModel(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str
