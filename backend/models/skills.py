from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
)


def skills(Base):

    Skill = type(
        "Skill",
        (Base,),
        {
            "__tablename__": "skills",

            "id": Column(
                Integer,
                primary_key=True,
                index=True,
                autoincrement=True,
            ),

            "name": Column(
                String(150),
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

    return Skill
