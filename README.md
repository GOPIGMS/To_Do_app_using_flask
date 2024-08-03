
# Flask To-Do List Application

This is a simple Flask web application that allows users to manage a to-do list. The application uses MySQL to store tasks.

## Features

- Add tasks to the to-do list.
- Edit existing tasks.
- Delete tasks from the to-do list.
- Display all tasks.

## Prerequisites

- Python 3.x
- Flask
- Flask-MySQLdb
- MySQL server

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/flask-todo-app.git
    cd flask-todo-app
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install Flask Flask-MySQLdb
    ```

4. Set up the MySQL database:

    - Ensure MySQL server is running.
    - Create a database named `todo`.
    - Create a table named `tasks` with the following schema:

    ```sql
    CREATE TABLE tasks (
        task VARCHAR(255) NOT NULL PRIMARY KEY
    );
    ```

5. Update the MySQL configuration in the `app.py` file if necessary:

    ```python
    app.config["MYSQL_HOST"] = "localhost"
    app.config["MYSQL_USER"] = "root"
    app.config["MYSQL_PASSWORD"] = ""
    app.config["MYSQL_DB"] = "todo"
    ```

## Running the Application

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

## Application Routes

- `/` - Home route that displays all tasks and allows adding new tasks.
- `/edittask,<string:task>` - Route to edit an existing task.
- `/deletetask,<string:task>` - Route to delete an existing task.

## Project Structure

- `app.py` - The main application file.
- `templates/` - Directory containing HTML templates:
  - `todos.html` - Template for displaying and adding tasks.
  - `edittask.html` - Template for editing tasks.

## Example Usage

1. **Add a Task**: Enter a task in the input field on the home page and click the "Add Task" button.
2. **Edit a Task**: Click the "Edit" link next to a task, modify the task, and click "Update Task".
3. **Delete a Task**: Click the "Delete" link next to a task to remove it from the list.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [Flask-MySQLdb](https://flask-mysqldb.readthedocs.io/en/latest/)


