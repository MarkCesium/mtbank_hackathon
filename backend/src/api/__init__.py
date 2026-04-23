from fastapi import APIRouter

from src.api import auth, battlepass, friends, game, shop

api_router = APIRouter(prefix="/api")
api_router.include_router(auth.controllers.router)
api_router.include_router(battlepass.controllers.router)
api_router.include_router(friends.controllers.router)
api_router.include_router(game.controllers.router)
api_router.include_router(shop.controllers.router)
