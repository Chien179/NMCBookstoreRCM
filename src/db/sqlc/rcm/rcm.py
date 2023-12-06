# Code generated by sqlc. DO NOT EDIT.
# versions:
#   sqlc v1.24.0
# source: rcm.sql
import dataclasses
from typing import AsyncIterator, Iterator, List

import sqlalchemy
import sqlalchemy.ext.asyncio

from src.db.sqlc.rcm import models


GET_BOOKS_RCM = """-- name: get_books_rcm \\:many
select u.username,
    b.id,
    r.rating,
    b.name,
    b.price,
    b.author,
    b.publisher,
    b.image,
    b.quantity,
    b.description,
    string_agg(distinct g.name, ',') as category
from books as b
    inner join reviews as r on b.id = r.books_id
    INNER JOIN users as u ON r.username = u.username
    INNER JOIN books_genres as bg ON b.id = bg.books_id
    inner join genres as g on bg.genres_id = g.id
group by u.username,
    b.id,
    r.rating,
    b.name,
    b.price,
    b.author,
    b.publisher,
    b.quantity,
    b.image,
    b.description
"""


@dataclasses.dataclass()
class GetBooksRCMRow:
    username: str
    id: int
    rating: int
    name: str
    price: float
    author: str
    publisher: str
    image: List[str]
    quantity: int
    description: str
    category: memoryview


class Querier:
    def __init__(self, conn: sqlalchemy.engine.Connection):
        self._conn = conn

    def get_books_rcm(self) -> Iterator[GetBooksRCMRow]:
        result = self._conn.execute(sqlalchemy.text(GET_BOOKS_RCM))
        for row in result:
            yield GetBooksRCMRow(
                username=row[0],
                id=row[1],
                rating=row[2],
                name=row[3],
                price=row[4],
                author=row[5],
                publisher=row[6],
                image=row[7],
                quantity=row[8],
                description=row[9],
                category=row[10],
            )


class AsyncQuerier:
    def __init__(self, conn: sqlalchemy.ext.asyncio.AsyncConnection):
        self._conn = conn

    async def get_books_rcm(self) -> AsyncIterator[GetBooksRCMRow]:
        result = await self._conn.stream(sqlalchemy.text(GET_BOOKS_RCM))
        async for row in result:
            yield GetBooksRCMRow(
                username=row[0],
                id=row[1],
                rating=row[2],
                name=row[3],
                price=row[4],
                author=row[5],
                publisher=row[6],
                image=row[7],
                quantity=row[8],
                description=row[9],
                category=row[10],
            )