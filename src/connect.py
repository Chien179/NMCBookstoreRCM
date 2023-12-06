from src.config import config
from src.db.sqlc.rcm import rcm
from src.db.sqlc.user import user
from sqlalchemy import create_engine

engine = create_engine(config.POSTGRES_URI)
conn = engine.connect()
rcm_querier = rcm.Querier(conn)
user_querier = user.Querier(conn)
