from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BookRequest(_message.Message):
    __slots__ = ["name", "size"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    name: str
    size: int
    def __init__(self, name: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...

class Books(_message.Message):
    __slots__ = ["id", "name", "price", "image", "description", "author", "publisher", "quantity", "rating"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    price: float
    image: _containers.RepeatedScalarFieldContainer[str]
    description: str
    author: str
    publisher: str
    quantity: int
    rating: float
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., price: _Optional[float] = ..., image: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ..., author: _Optional[str] = ..., publisher: _Optional[str] = ..., quantity: _Optional[int] = ..., rating: _Optional[float] = ...) -> None: ...

class BookResponse(_message.Message):
    __slots__ = ["books"]
    BOOKS_FIELD_NUMBER: _ClassVar[int]
    books: _containers.RepeatedCompositeFieldContainer[Books]
    def __init__(self, books: _Optional[_Iterable[_Union[Books, _Mapping]]] = ...) -> None: ...
