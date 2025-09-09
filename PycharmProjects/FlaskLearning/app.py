from pydantic import BaseModel, Field
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for
from flask_scss import Scss
from pymongo import MongoClient, ReturnDocument


app = Flask(__name__)
Scss(app)


URI = "mongodb://localhost:27017/"
client = MongoClient(URI)
db = client['my_database']
tasks_collection = db["tasks"]
id_counter = db['id_counter']


def get_id():
    counter = id_counter.find_one_and_update(
        {'_id': 'taskid'},
        {'$inc': {'seq': 1}},
        upsert=True,
        return_document=ReturnDocument.AFTER 
    )
    return counter['seq']

class Task(BaseModel):
    id: int = Field(default_factory=get_id)
    content: str
    completed: bool = False
    created_At: datetime = Field(default_factory=datetime.now)


@app.route('/', methods=['POST', 'GET'])
def home():
    #Add a task
    if request.method == 'POST':
        current_task = request.form['content']
        new_task = Task(content=current_task)
        
        try:
            #Save to DB
            tasks_collection.insert_one(new_task.model_dump())
            return redirect('/')
        except Exception as e:
            print(f'Error: {e}')
            return f'Error: {e}'

    #Show all current tasks
    else:
        #fetch tasks from DB
        docs = tasks_collection.find({}, {"_id": 0}).sort('created_At', 1)
        tasks = [Task(**task) for task in docs]
        return render_template('index.html', tasks=tasks)
    
#Delete a task
@app.route('/delete/<int:id>')
def delete(id):
    try:
        tasks_collection.delete_one({'id': int(id)})
        return redirect('/')
    except Exception as e:
        return f'Error deleting task: {e}'
    
    
# Update a task
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    task = tasks_collection.find_one({'id': int(id)}, {"_id": 0})

    if not task:
        return 'Task not found', 404

    if request.method == 'POST':
        new_content = request.form['content']
        try:
            tasks_collection.update_one(
                {'id': int(id)},
                {'$set': {'content': new_content}}
            )
            return redirect('/')
        except Exception as e:
            return f'Error editing task: {e}'

    return render_template('edit.html', task=task)



 
 
 
 
 
 
    
    
    
    
if __name__ == '__main__':
    app.run(debug=True)
