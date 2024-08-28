from fastapi import APIRouter

from db import engine, Base
from routes.files import files_router
from routes.login import login_router
from routes.users import users_router
from routes.answers import answers_router
from routes.categories import categories_router
from routes.finalresults import final_results_router
from routes.questions import questions_router
from routes.results import results_router
from routes.sciences import sciences_router


api = APIRouter()

Base.metadata.create_all(bind=engine)


api.include_router(login_router)
api.include_router(users_router)
api.include_router(categories_router)
api.include_router(sciences_router)
api.include_router(questions_router)
api.include_router(answers_router)
api.include_router(results_router)
api.include_router(final_results_router)
api.include_router(files_router)
