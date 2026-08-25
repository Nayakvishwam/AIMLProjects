from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    UniqueConstraint,
)


def skills_candidates_lines(Base):

    SkillCandidateLine = type(
        "SkillCandidateLine",
        (Base,),
        {
            "__tablename__": "skills_candidates_lines",

            "__table_args__": (
                UniqueConstraint(
                    "skill_id",
                    "candidate_id",
                    name="uq_skill_candidate",
                ),
            ),

            "id": Column(
                Integer,
                primary_key=True,
                index=True,
                autoincrement=True,
            ),

            "skill_id": Column(
                Integer,
                ForeignKey(
                    "skills.id",
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

    return SkillCandidateLine
