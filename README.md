# devops-tasks
tasks project at devops studies

# Tasks Project

This project is a simple REST API built with Flask that enables users to manage tasks. Users can perform CRUD (Create, Read, Update, Delete) operations on tasks, with each task consisting of a title and some details.

## Getting Started

To get started with this project, follow the instructions below.

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository:

git clone https://github.com/your-username/tasks-project.git

2. Navigate to the project directory:

cd tasks-project

3. Install the dependencies:

pip install -r requirements.txt

4. Run the Flask application:

python app.py

The application should now be running on http://127.0.0.1:5000/.

### Usage

You can interact with the REST API using curl or any other HTTP client. Here are some examples of how to use it with curl:

#### Get all tasks:

curl http://127.0.0.1:5000/tasks

#### get a specific task:

curl http://127.0.0.1:5000/tasks/<task_id>

#### Add a new task:

curl -X POST -H "Content-Type: application/json" -d '{"title": "New Task", "details": "Task details"}' http://127.0.0.1:5000/tasks

#### Update an existing task:

curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Task", "details": "Updated details"}' http://127.0.0.1:5000/tasks/<task_id>

#### Delete a task:

curl -X DELETE http://127.0.0.1:5000/tasks/<task_id>

