from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    UniqueConstraint,
)


def keywords_candidate_lines(Base):

    KeywordCandidateLine = type(
        "KeywordCandidateLine",
        (Base,),
        {
            "__tablename__": "keywords_candidate_lines",

            "__table_args__": (
                UniqueConstraint(
                    "keyword_id",
                    "candidate_id",
                    name="uq_keyword_candidate",
                ),
            ),

            "id": Column(
                Integer,
                primary_key=True,
                index=True,
                autoincrement=True,
            ),

            "keyword_id": Column(
                Integer,
                ForeignKey(
                    "keywords.id",
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
        },
    )

    return KeywordCandidateLine
