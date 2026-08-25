from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
)


def universities(Base):

    University = type(
        "University",
        (Base,),
        {
            "__tablename__": "universities",

            "id": Column(
                Integer,
                primary_key=True,
                index=True,
                autoincrement=True,
            ),

            "name": Column(
                String(200),
                nullable=False,
                unique=True,
                index=True,
            ),

            "description": Column(
                Text,
                nullable=True,
            ),

            "website": Column(
                String(500),
                nullable=True,
                index=True,
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

    return University
