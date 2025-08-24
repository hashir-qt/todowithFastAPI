from typing import List
from fastapi import FastAPI, HTTPException
from models import Priority, Todo, TodoCreate, TodoUpdate

api = FastAPI()

all_todos = [
        Todo(todo_id=1, todo_name= "Sports", todo_description= "Go to the gym and train till failure", priority=Priority.HIGH),
        Todo(todo_id=2, todo_name= "Study", todo_description= "Explore Java",  priority=Priority.HIGH),
        Todo(todo_id=3, todo_name= "'Education", todo_description= "'Go to University",  priority=Priority.MEDIUM),
        Todo(todo_id=4, todo_name= "Python Project", todo_description= " Work on project",  priority=Priority.LOW)
        ]
#GET all todos
@api.get('/todos', response_model=List[Todo])
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos 



# localhost:5000/todos?firstn=3
@api.get('/todos/{todo_id}', response_model=Todo)
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo
        

@api.post('/todos', response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo_id = max(todo.todo_id for todo in all_todos) + 1
    
    new_todo = Todo(
                todo_id= new_todo_id,
                todo_name= todo.todo_name,
                todo_description= todo.todo_description,
                priority= todo.priority
    )

    all_todos.append(new_todo)
    return new_todo


@api.put('/todos/{todo_id}', response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
     if todo.todo_id == todo_id:
         todo.todo_name = updated_todo.todo_name,
         todo.todo_description = updated_todo.todo_description,
         todo.priority = updated_todo.priority
         return todo
    return HTTPException(status_code=404, detail="'Todo not found")


@api.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo['todo_id'] == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo
    return HTTPException(status_code=404, detail="'Todo not found")
