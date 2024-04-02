from flask import Flask, json, request
import tasks_db
app = Flask(__name__)


#get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks=tasks_db.get_all_tasks()
    return json.dumps(tasks)

#get task by id
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    tasks=tasks_db.get_all_tasks()
    task=[task for task in tasks["tasks"] if task['id'] == task_id]
    if (task):        
       return json.dumps(task)
    return json.dumps({'error': 'TaskNotFound'}),404

#add task
@app.route('/tasks', methods=['POST'])
def add_task():
    if not request.json or 'title' not in request.json:
        return json({'error': 'this is not a task!'}),404
    tasks_db.add_task(request.json['title'],request.json['details'])
    return json.dumps(tasks_db.get_all_tasks()),201

#update task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    
     if not request.json or 'title' not in request.json:
        return json({'error': 'this is not a task!'}),404 
     if tasks_db.update_task(task_id,request.json) == 'TaskNotFound':
         return json.dumps({'error': 'TaskNotFound'}),404
     
     return json.dumps(tasks_db.get_all_tasks()),201

#delete task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    
     if tasks_db.del_task(task_id) == 'TaskNotFound':
         return json.dumps({'error': 'TaskNotFound'}),404
     
     return json.dumps(tasks_db.get_all_tasks()),201


# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
    
