import  json, json_files
jfilename = 'tasks.json'

     
def get_all_tasks():
    return json_files.get_tasks_fromfile(jfilename)

def add_task(desc,detail):

   tasks = json_files.get_tasks_fromfile(jfilename)
#create new task_id 
   if tasks and len(tasks["tasks"])>0:
       new_task_id = max(task['id'] for task in tasks["tasks"]) +1
   else:
       new_task_id=1       

   task = {
        "id": new_task_id, 
        "title": desc,
        "details": detail
    }
   tasks["tasks"].append(task)
   json_files.update_tasks_file(jfilename, tasks)
    
def del_task(task_id):
     tasks = json_files.get_tasks_fromfile(jfilename)
    #i=0
    #  for task in tasks["tasks"]:
    #     if task['id']==task_id:            
    #         break
    #     i+=1

     task=next((task for task in tasks["tasks"] if task['id'] == task_id),None)
     if task:
        del(tasks["tasks"][i])
        json_files.update_tasks_file(jfilename, tasks)
     else:
         return 'TaskNotFound' 

def update_task(task_id,data):

    tasks = json_files.get_tasks_fromfile(jfilename)
    task=[task for task in tasks["tasks"] if task['id'] == task_id]
    if len(task) == 0:
        return 'TaskNotFound' 

    task.update(data)
    json_files.update_tasks_file(jfilename, tasks)
    
