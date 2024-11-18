from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import config

engine = create_engine(config.database_url, pool_size=15, echo=False)
SessionLocal = sessionmaker(autocommit=False, bind=engine, autoflush=False)


def get_session():
    try:
        session = SessionLocal()
        return session
    except Exception:
        session.rollback()
    finally:
        session.close()


@contextmanager
def get_db_context():
    session = SessionLocal()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


class Base(DeclarativeBase):
    # Generate __tablename__ automatically
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
