from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import os
from dotenv import load_dotenv
from models import initModels


# Load variables from .env
load_dotenv()


def get_required_env(name: str) -> str:
    """
    Get a required environment variable.

    Raises:
        RuntimeError: If the variable is missing or empty.
    """

    value = os.getenv(name)

    if not value:
        raise RuntimeError(
            f"Required environment variable '{name}' is not set."
        )

    return value


def generate_database_url() -> str:
    """
    Generate PostgreSQL SQLAlchemy connection URL.
    """

    user = get_required_env("POSTGRES_USER")
    password = get_required_env("POSTGRES_PASSWORD")
    host = get_required_env("POSTGRES_HOST")
    port = get_required_env("POSTGRES_PORT")
    database = get_required_env("POSTGRES_DATABASE")

    return (
        f"postgresql+psycopg://"
        f"{user}:{password}@{host}:{port}/{database}"
    )


DATABASE_URL = generate_database_url()


class Base(DeclarativeBase):
    pass


engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


dbModels = initModels(Base)
