from .candidates import candidate
from .industries import industries
from .countries import countries
from .states import states
from .cities import cities
from .degress import degrees
from .degrees_candidate_lines import degrees_candidate_lines
from .keywords import keywords
from .projects import projects
from .skills import skills
from .skills_candidates_lines import skills_candidates_lines
from .universities import universities
from .users import users


def initModels(Base):
    models = {}
    models["candidates"] = candidate(Base=Base)
    models["industries"] = industries(Base=Base)
    models["countries"] = countries(Base=Base)
    models["states"] = states(Base=Base)
    models["cities"] = cities(Base=Base)
    models["degrees"] = degrees(Base=Base)
    models["degrees_candidate_lines"] = degrees_candidate_lines(Base=Base)
    models["keywords"] = keywords(Base=Base)
    models["projects"] = projects(Base=Base)
    models["skills"] = skills(Base=Base)
    models["skills_candidates_lines"] = skills_candidates_lines(Base=Base)
    models["universities"] = universities(Base=Base)
    models["users"] = users(Base=Base)
    return models
