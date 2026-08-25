from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Numeric,
)


def states(Base):

    State = type(
        "State",
        (Base,),
        {
            "__tablename__": "states",

            "id": Column(
                Integer,
                primary_key=True,
                index=True,
                autoincrement=True,
            ),

            # Relation → countries.id
            "country_id": Column(
                Integer,
                ForeignKey(
                    "countries.id",
                    ondelete="CASCADE",
                ),
                nullable=False,
                index=True,
            ),

            "name": Column(
                String(100),
                nullable=False,
                index=True,
            ),

            "iso2": Column(
                String(10),
                nullable=True,
                index=True,
            ),

            "iso3166_2": Column(
                String(10),
                nullable=True,
                unique=True,
                index=True,
            ),

            "native": Column(
                String(200),
                nullable=True,
            ),

            "latitude": Column(
                Numeric(10, 7),
                nullable=True,
            ),

            "longitude": Column(
                Numeric(10, 7),
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

    return State
