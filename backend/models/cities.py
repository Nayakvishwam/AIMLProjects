from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Numeric,
)


def cities(Base):

    City = type(
        "City",
        (Base,),
        {
            "__tablename__": "cities",

            "id": Column(
                Integer,
                primary_key=True,
                index=True,
                autoincrement=True,
            ),

            # Relation → states.id
            "state_id": Column(
                Integer,
                ForeignKey(
                    "states.id",
                    ondelete="CASCADE",
                ),
                nullable=False,
                index=True,
            ),

            "name": Column(
                String(150),
                nullable=False,
                index=True,
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

    return City
