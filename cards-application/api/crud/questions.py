from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Sequence

from core.models import Question
from core.schemas.question import QuestionCreate, QuestionRead


async def get_all_questions(session: AsyncSession) -> Sequence[Question]:
    statement = select(Question).order_by(Question.id)
    result = await session.scalars(statement)
    return result.all()

async def get_question_by_id(session: AsyncSession, id: int):
    statement = select(Question).filter(Question.id == id)
    result = await session.execute(statement)
    return result.scalars().one()

async def create_question(session: AsyncSession, question_create: QuestionCreate) -> Question:
     question = Question(
         title=question_create.title,
         answer=question_create.answer
     )
     session.add(question)
     await session.commit()
     return question


async def delete_question(session: AsyncSession, id:int) -> Question:
    result = await get_question_by_id(session, id)
    await session.delete(result)
    await session.commit()
    return result



