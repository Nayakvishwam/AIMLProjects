from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)


def countries(Base):

    Country = type(
        "Country",
        (Base,),
        {
            "__tablename__": "countries",

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

            "iso3": Column(
                String(3),
                nullable=False,
                unique=True,
                index=True,
            ),

            "iso2": Column(
                String(2),
                nullable=False,
                unique=True,
                index=True,
            ),

            "numeric_code": Column(
                String(3),
                nullable=False,
                unique=True,
                index=True,
            ),

            "phonecode": Column(
                String(10),
                nullable=True,
                index=True,
            ),

            "capital": Column(
                String(100),
                nullable=True,
            ),

            "currency": Column(
                String(3),
                nullable=True,
            ),

            "currency_name": Column(
                String(100),
                nullable=True,
            ),

            "currency_symbol": Column(
                String(10),
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

    return Country
