from pydantic import BaseModel


class RCMSchema(BaseModel):
    id: int
    user_id: int
    rating: float
    price: float
    name: str
    author: str
    publisher: str
    image: list
    quantity: int
    is_deleted: bool
    description: str
    category: str
