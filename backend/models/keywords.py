from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
)
from datetime import datetime


def keywords(Base):

    Keyword = type(
        "Keyword",
        (Base,),
        {
            "__tablename__": "keywords",

            "id": Column(
                Integer,
                primary_key=True,
                index=True,
                autoincrement=True,
            ),

            "name": Column(
                String(100),
                nullable=False,
                unique=True,
                index=True,
            ),

            "description": Column(
                Text,
                nullable=True,
            ),

            "created_at": Column(
                DateTime,
                default=datetime.utcnow,
                nullable=False,
            ),

            "updated_at": Column(
                DateTime,
                default=datetime.utcnow,
                onupdate=datetime.utcnow,
                nullable=False,
            ),
        },
    )

    return Keyword
