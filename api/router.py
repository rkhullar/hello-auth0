from fastapi import APIRouter

from .routes import debug

router = APIRouter()
router.include_router(debug.router, prefix='/debug', tags=['debug'])
