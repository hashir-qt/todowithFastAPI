from fastapi import FastAPI

api = FastAPI()

all_todos = [
    {'todo_id': 1, 'todo_name': 'Sports', 'todo_description': 'Go to the gym and train till failure'},
    {'todo_id': 2, 'todo_name': 'Study', 'todo_description': 'Explore Java'},
    {'todo_id': 3, 'todo_name': 'Education', 'todo_description': 'Go to University'},
    {'todo_id': 4, 'todo_name': 'Python Project', 'todo_description': ' Work on project'}
]

# GET, POST, PUT, DELETE

@api.get('/')
def home():
    return {"message": "Hello World!"}

# localhost:5000/todos?firstn=3

@api.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo ['todo_id'] == todo_id:
            return {'result': todo}
        

@api.get('/todos')
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos 


@api.post('/todos')
def create_todo(todo: dict):
    new_todo_id = max(todo['todo_id'] for todo in all_todos) + 1

    new_todo = {
        'todo_id': new_todo_id,
        'todo_name': todo['todo_name'],
        'todo_description': todo['todo_description']
    }

    all_todos.append(new_todo)
    return new_todo


@api.put('/todos/{todo_id}')
def update_todo(todo_id: int, updated_todo: dict):
    for todo in all_todos:
     if todo['todo_id'] == todo_id:
        todo['todo_name'] = updated_todo['todo_name']
        todo['todo_description'] = updated_todo['todo_description']
        return todo
    return "Error, NOT FOUND"


@api.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo['todo_id'] == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo
    return "Error, NOT FOUND"