from fastapi import APIRouter

from core.config import settings

from api.questions import router as questions_router
router = APIRouter(
    prefix=settings.api.prefix,
)
router.include_router(questions_router,prefix=settings.api.questions)