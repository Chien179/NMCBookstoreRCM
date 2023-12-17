from src.lib.logger import DefaultFormatter
import logging
from src.config import config
import grpc
from src.pb.rcm_pb2_grpc import add_BookRecommendServicer_to_server
from src.helper.rcm import RCMHelper
from src.lib.logger import logger

# Coroutines to be invoked when the event loop is shutting down.
_cleanup_coroutines = []


async def serve() -> None:
    server = grpc.aio.server()
    add_BookRecommendServicer_to_server(RCMHelper(), server)
    listen_addr = f"[::]:{config.PORT}"
    server.add_insecure_port(listen_addr)
    logger.info("Starting server on %s", listen_addr)
    await server.start()

    async def server_graceful_shutdown():
        logger.info("Starting graceful shutdown...")
        # Shuts down the server with 5 seconds of grace period. During the
        # grace period, the server won't accept new connections and allow
        # existing RPCs to continue within the grace period.
        await server.stop(5)

    _cleanup_coroutines.append(server_graceful_shutdown())
    await server.wait_for_termination()
