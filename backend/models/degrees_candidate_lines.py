from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
)


def degrees_candidate_lines(Base):

    DegreeCandidateLine = type(
        "DegreeCandidateLine",
        (Base,),
        {
            "__tablename__": "degrees_candidate_lines",

            "id": Column(
                Integer,
                primary_key=True,
                index=True,
                autoincrement=True,
            ),

            "degree_id": Column(
                Integer,
                ForeignKey(
                    "degrees.id",
                    ondelete="CASCADE",
                ),
                nullable=False,
                index=True,
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
            "university_id": Column(
                Integer,
                ForeignKey(
                    "universities.id",
                    ondelete="CASCADE",
                ),
                nullable=False,
                index=True,
            ),
        },
    )

    return DegreeCandidateLine
