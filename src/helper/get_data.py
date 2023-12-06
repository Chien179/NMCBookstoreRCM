from src.connect import rcm_querier, user_querier
from src.schemas.rcm import RCMSchema


def get_data():
    books = []
    books_rcm = rcm_querier.get_books_rcm()
    users = user_querier.get_users()

    user_ids = {user: i + 1 for i, user in enumerate(users)}
    for book in books_rcm:
        b = RCMSchema(
            id=book.id,
            user_id=user_ids.get(book.username),
            name=book.name,
            price=book.price,
            image=book.image,
            description=book.description,
            author=book.author,
            publisher=book.publisher,
            quantity=book.quantity,
            rating=book.rating,
            category=book.category,
        ).model_dump()
        books.append(b)

    return books
