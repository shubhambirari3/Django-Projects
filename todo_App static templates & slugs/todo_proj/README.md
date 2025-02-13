# Django To-Do App

This is a simple To-Do application built with Django. It allows users to create, update, delete, and mark tasks as complete.

## Features

- Create new tasks with a title and note.
- View a list of all tasks.
- Update existing tasks.
- Delete tasks with a confirmation step.
- Mark tasks as complete or incomplete.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/todo_app.git
    cd todo_app
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Open your web browser and go to `http://127.0.0.1:8000/task_list/` to view the app.

## Usage

- **Create Task**: Click on the "Create New Task" button to add a new task.
- **Update Task**: Click on the "Update" button next to a task to edit its details.
- **Delete Task**: Click on the "Delete" button next to a task to delete it. You will be asked to confirm the deletion.
- **Mark Task as Complete**: Check or uncheck the "Completed" checkbox to mark a task as complete or incomplete.

## Project Structure

```
todo_proj/
├── todo_app/
│   ├── migrations/
│   ├── templates/
│   │   └── todo_app/
│   │       ├── task_create.html
│   │       ├── task_delete.html
│   │       ├── task_list.html
│   │       └── task_update.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── todo_proj/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

#                                    ---* THANK YOU *---
                                                 
                                                 -Shubham_Birari
