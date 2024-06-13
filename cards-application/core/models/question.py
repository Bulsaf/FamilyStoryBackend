import uuid

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class Question(Base):
    __tablename__ = "questions"
    title: Mapped[str] = mapped_column(nullable=False)
    answer: Mapped[str] = mapped_column(nullable=False)