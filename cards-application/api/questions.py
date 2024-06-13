from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models import db_helper
from core.schemas.question import QuestionRead, QuestionCreate
from api.crud.questions import create_question, get_all_questions, delete_question

router = APIRouter(tags=["Questions"])


@router.get("", response_model=list[QuestionRead])
async def get_questions(session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ]):
    questions = await get_all_questions(session=session)
    return questions

@router.post("", response_model=QuestionRead)
async def create_questions(session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter)], question_create: QuestionCreate):
    question = await create_question(session=session, question_create=question_create)
    return question

@router.delete("", response_model=QuestionRead)
async def delete_questions(session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter)], id: int):
    question = await delete_question(session,id)
    return question



