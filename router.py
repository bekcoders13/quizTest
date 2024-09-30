from fastapi import APIRouter

from db import engine, Base
from routes.files import files_router
from routes.answers import answers_router
from routes.categories import categories_router
from routes.questions import questions_router
from routes.results import results_router
from routes.sciences import sciences_router
from routes.options import options_router
from routes.login import login_router
from routes.tests import tests_router
from routes.user import users_router
from routes.teacher import teachers_router
from routes.course import courses_router
from routes.app_about import app_about_router

api = APIRouter()

Base.metadata.create_all(bind=engine)

api.include_router(login_router)
api.include_router(users_router)
api.include_router(categories_router)
api.include_router(sciences_router)
api.include_router(options_router)
api.include_router(questions_router)
api.include_router(answers_router)
api.include_router(tests_router)
api.include_router(results_router)
api.include_router(files_router)
api.include_router(teachers_router)
api.include_router(courses_router)
api.include_router(app_about_router)
