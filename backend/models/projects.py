from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
)


def projects(Base):

    Project = type(
        "Project",
        (Base,),
        {
            "__tablename__": "projects",

            "id": Column(
                Integer,
                primary_key=True,
                index=True,
                autoincrement=True,
            ),

            "candidate_id": Column(
                Integer,
                ForeignKey(
                    "candidates.id",
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

            "description": Column(
                Text,
                nullable=True,
            ),

            "url": Column(
                String(500),
                nullable=True,
                index=True,
            ),

            "start_date": Column(
                DateTime,
                nullable=True,
            ),

            "end_date": Column(
                DateTime,
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

    return Project
