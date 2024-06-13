from pydantic import BaseModel

class QuestionBase(BaseModel):
    title: str
    answer: str

class QuestionCreate(QuestionBase):
    pass

class QuestionRead(QuestionBase):
    id: int