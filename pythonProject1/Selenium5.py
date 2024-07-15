from flask import Flask, request, jsonify

# Create a Flask application
app = Flask(__name__)

# Sample data (could be replaced with database operations)
tasks = [
    {"id": 1, "title": "Task 1", "description": "Sample task 1"},
    {"id": 2, "title": "Task 2", "description": "Sample task 2"}
]
next_task_id = 3

# Route to get all tasks or create a new task
@app.route('/tasks', methods=['GET', 'POST'])
def all_tasks():
    if request.method == 'GET':
        return get_all_tasks()
    elif request.method == 'POST':
        return create_task()

# Route to get, update or delete a specific task
@app.route('/tasks/<int:task_id>', methods=['GET', 'PUT', 'DELETE'])
def single_task(task_id):
    if request.method == 'GET':
        return get_task(task_id)
    elif request.method == 'PUT':
        return update_task(task_id)
    elif request.method == 'DELETE':
        return delete_task(task_id)

def get_all_tasks():
    return jsonify(tasks)

def create_task():
    global next_task_id
    new_task = {
        "id": next_task_id,
        "title": request.json.get('title', ''),
        "description": request.json.get('description', '')
    }
    tasks.append(new_task)
    next_task_id += 1
    return jsonify(new_task), 201

def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)

def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    return jsonify(task)

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({"message": "Task deleted"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)