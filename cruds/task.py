from typing import Optional
from schemas import TaskCreate, TaskStatus, TaskUpdate

class Task:
  def __init__(
      self,
      id: int,
      name: str,
      description: Optional[str],
      status: TaskStatus
  ):
    self.id = id
    self.name = name
    self.description = description
    self.status = status

tasks = [
  Task(1, "勉強", "前回の終了地点から", TaskStatus.UNCOMPLETED),
  Task(2, "運動", None, TaskStatus.UNCOMPLETED),
  Task(3, "買い物", None, TaskStatus.UNCOMPLETED),
]

def find_all():
  return tasks

def find_by_id(id: int):
  for task in tasks:
    if task.id == id:
      return task
  return None

def find_by_name(name: str):
  filtered_tasks = []

  for task in tasks:
    if task.name in name:
      filtered_tasks.append(task)
  return filtered_tasks

def create(task_create: TaskCreate):
  new_task = Task(
    len(tasks) + 1,
    task_create.name,
    task_create.description,
    TaskStatus.UNCOMPLETED,
  )
  new_task.append(new_task)
  return new_task

def update(id: int, task_update: TaskUpdate):
  for task in tasks:
    if task.id == id:
      task.name = task.name if task_update.name is None else task_update.name
      task.description = task.description if task_update.description is None else task_update.description
      task.status = task.status if task_update.status is None else task_update.status
      return task
  return None

def delete(id: int):
  for i in range(len(tasks)):
    if tasks[i].id == id:
      delete_task = tasks.pop(i)
      return delete_task
  return None