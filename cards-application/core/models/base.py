from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, declared_attr

from core.config import settings

from utils import camel_case_to_snake_case

class Base(DeclarativeBase):
    metadata = MetaData(
        naming_convention=settings.db.naming_convention
    )
    id: Mapped[int] = mapped_column(primary_key=True)
    