from fastapi import APIRouter

from src.api import auth, game

api_router = APIRouter(prefix="/api")
api_router.include_router(auth.controllers.router)
api_router.include_router(game.controllers.router)
