from src.pb.rcm_pb2_grpc import BookRecommendServicer
from src.pb.rcm_pb2 import BookRequest, BookResponse, Books
from grpc.aio import ServicerContext
from src.helper.rcm_book import RCMBookHelper
from src.lib.logger import logger


class RCMHelper(BookRecommendServicer):
    async def GetBookRecommend(
        self, request: BookRequest, context: ServicerContext
    ) -> BookResponse:
        req = request
        rcm = RCMBookHelper()
        books_rcm = rcm.content_based_recommender(req.name, req.size)
        results = BookResponse()
        for book in books_rcm:
            b = Books(
                id=book.get("id"),
                name=book.get("name"),
                price=book.get("price"),
                image=book.get("image"),
                description=book.get("description"),
                author=book.get("author"),
                publisher=book.get("publisher"),
                quantity=book.get("quantity"),
                rating=book.get("rating"),
            )
            results.books.append(b)
        if not results:
            return None

        logger.debug("Get recommend books success")
        return results
