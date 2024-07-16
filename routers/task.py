from fastapi import APIRouter, Path, Query, HTTPException, Depends
from cruds import task as task_cruds
from schemas import TaskCreate, TaskUpdate, TaskResponse
from starlette import status
from database import get_db
from typing import Annotated
from sqlalchemy.orm import Session

# dbDependencyはsqlalchemyのセッション型となり、get_db関数から取得されるセッションが注入される
dbDependency = Annotated[Session, Depends(get_db)]

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("", response_model=list[TaskResponse], status_code=status.HTTP_200_OK)
async def find_all(db: dbDependency):
  return task_cruds.find_all(db)

@router.get("/{id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
async def find_by_id(db: dbDependency, id: int=Path(gt=0)):
  found_task = task_cruds.find_by_id(db, id)
  if not found_task:
    raise HTTPException(status_code=404, detail="Task noy found")
  return found_task

@router.get("/", response_model=list[TaskResponse], status_code=status.HTTP_200_OK)
async def find_by_name(db: dbDependency, name: str = Query(min_length=1, max_length=20)):
  return task_cruds.find_by_name(db, name)

@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
# task_create=Body()とすることで、リクエストのBody要素をcreate-itemとして利用していたが、
# スキーマをcreate関数の引数の型として指定することで、
# リクエストのBodyの内容がスキーマの制約に適合しているかの自動チェックが入る
async def create(db: dbDependency, task_create: TaskCreate):
  return task_cruds.create(db, task_create)

@router.put("/{id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
async def update(db: dbDependency, task_update: TaskUpdate, id: int=Path(gt=0)):
  updated_task = task_cruds.update(db, id, task_update)
  if not updated_task:
    raise HTTPException(status_code=404, detail="Task not updated")
  return updated_task

@router.delete("/{id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
async def delete(db: dbDependency, id: int=Path(gt=0)):
  deleted_task = task_cruds.delete(db, id)
  if not deleted_task:
    raise HTTPException(status_code=404, detail="Task not deleted")
  return deleted_task