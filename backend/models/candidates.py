from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)


def candidate(Base):

    Candidate = type(
        "Candidate",
        (Base,),
        {
            "__tablename__": "candidates",

            "id": Column(
                Integer,
                primary_key=True,
                index=True,
                autoincrement=True
            ),

            "name": Column(
                String,
                index=True,
                nullable=False
            ),

            "email": Column(
                String,
                nullable=False
            ),
            "phone": Column(
                String(20),
                nullable=False
            ),

            "linkedin": Column(
                String(500),
                index=True
            ),

            "github": Column(
                String(500),
                index=True
            ),
            "industry_id": Column(
                Integer,
                ForeignKey("industries.id"),
                nullable=False,
                index=True
            ),
            "created_at": Column(
                DateTime,
                default=datetime.utcnow,
            ),

            "updated_at": Column(
                DateTime,
                default=datetime.utcnow,
                onupdate=datetime.utcnow,
            )
        },
    )

    return Candidate
