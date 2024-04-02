import os,json

def get_tasks_fromfile(filename):    
   if not os.path.exists(filename):
       with open(filename,"w")as jfile:
           json.dump([],jfile)
   with open(filename,"r") as jfile:      
      json_content = json.load(jfile)
   jfile.close()
   return json_content

def update_tasks_file(filename,json_content):
    with open(filename, 'w') as file:
        file.write(json.dumps(json_content))
        file.close
   