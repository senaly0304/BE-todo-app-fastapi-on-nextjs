from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from enum import Enum
from datetime import datetime

class TaskStatus(Enum):
  COMPLETED = "COMPLETED"
  UNCOMPLETED = "UNCOMPLETED"

class TaskCreate(BaseModel):
  name: str = Field(min_length=1, max_length=20, examples=["買い物に行く"])
  description: Optional[str] = Field(default=None, examples=["卵、牛乳、お菓子を買う"])

class TaskUpdate(BaseModel):
  name: Optional[str] = Field(None, min_length=1, max_length=20, examples=["資格の勉強をする"])
  description: Optional[str] = Field(None, examples=["p.20から行う"])
  status: Optional[TaskStatus] = Field(None, examples=[TaskStatus.COMPLETED])

class TaskResponse(BaseModel):
  id: int = Field(gt=0, examples=[1])
  name: str = Field(min_length=1, max_length=20, examples=["買い物に行く"])
  description: Optional[str] = Field(None, examples=["卵、牛乳、お菓子を買う"])
  status: TaskStatus = Field(examples=[TaskStatus.UNCOMPLETED])
  created_at: datetime
  updated_at: datetime

  model_config = ConfigDict(from_attributes=True)