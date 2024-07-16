from schemas import TaskCreate, TaskUpdate
from sqlalchemy.orm import Session
from models import Task

def find_all(db: Session):
  return db.query(Task).all()

def find_by_id(db: Session, id: int):
  return db.query(Task).filter(Task.id == id).first()

def find_by_name(db: Session, name: str):
  return db.query(Task).filter(Task.name.like(f"%{name}%"))

def create(db: Session, task_create: TaskCreate):
  new_task = Task(
    **task_create.model_dump()
  )
  db.add(new_task)
  db.commit()
  return new_task

def update(db: Session, id: int, task_update: TaskUpdate):
  task = find_by_id(db, id)
  if task is None:
    return None
  
  task.name = task.name if task_update.name is None else task_update.name
  task.description = task.description if task_update.description is None else task_update.description
  task.status = task.status if task_update.status is None else task_update.status

  db.add(task)
  db.commit()
  return task

def delete(db: Session, id: int):
  task = find_by_id(db, id)
  if task is None:
    return None
  
  db.delete(task)
  db.commit()
  return task