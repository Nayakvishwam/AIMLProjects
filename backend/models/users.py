from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
)


def users(Base):

    User = type(
        "User",
        (Base,),
        {
            "__tablename__": "users",

            "id": Column(
                Integer,
                primary_key=True,
                index=True,
                autoincrement=True,
            ),

            "name": Column(
                String(150),
                nullable=False,
                index=True,
            ),

            "email": Column(
                String(255),
                nullable=False,
                unique=True,
                index=True,
            ),

            "password": Column(
                String(255),
                nullable=False,
            ),

            "phone": Column(
                String(20),
                nullable=True,
                index=True,
            ),

            "active": Column(
                Boolean,
                nullable=False,
                default=True,
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

    return User