from fastapi import APIRouter, Path, Query, HTTPException
from cruds import task as task_cruds
from schemas import TaskCreate, TaskUpdate, TaskResponse
from starlette import status

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("", response_model=list[TaskResponse], status_code=status.HTTP_200_OK)
async def find_all():
  return task_cruds.find_all()

@router.get("/{id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
async def find_by_id(id: int=Path(gt=0)):
  found_task = task_cruds.find_by_id(id)
  if not found_task:
    raise HTTPException(status_code=404, detail="Task noy found")
  return found_task

@router.get("/", response_model=list[TaskResponse], status_code=status.HTTP_200_OK)
async def find_by_name(name: str = Query(min_length=1, max_length=20)):
  return task_cruds.find_by_name(name)

@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
# task_create=Body()とすることで、リクエストのBody要素をcreate-itemとして利用していたが、
# スキーマをcreate関数の引数の型として指定することで、
# リクエストのBodyの内容がスキーマの制約に適合しているかの自動チェックが入る
async def create(task_create: TaskCreate):
  return task_cruds.create(task_create)

@router.put("/{id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
async def update(task_update: TaskUpdate, id: int=Path(gt=0)):
  updated_task = task_cruds.update(id, task_update)
  if not updated_task:
    raise HTTPException(status_code=404, detail="Task not updated")
  return updated_task

@router.delete("/{id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
async def delete(id: int=Path(gt=0)):
  deleted_task = task_cruds.delete(id)
  if not deleted_task:
    raise HTTPException(status_code=404, detail="Task not deleted")
  return deleted_task