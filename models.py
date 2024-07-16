from database import Base
from sqlalchemy import Column, Integer, String, Enum, DateTime
from schemas import TaskStatus
from datetime import datetime

class Task(Base):
  __tablename__ = "tasks"
  
  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  description = Column(String, nullable=True)
  status = Column(Enum(TaskStatus), nullable=False, default=TaskStatus.UNCOMPLETED)
  created_at = Column(DateTime, default=datetime.now())
  updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
  