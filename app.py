from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# --- MongoDB Connection Setup ---
client = MongoClient('mongodb://localhost:27017/')
db = client['todo_database']
collection = db['todo_items']
# --------------------------------

# Code from master_1
@app.route('/todo')
def todo_page():
    return render_template('todo.html')

# Code from master_2
@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form['itemName']
    item_description = request.form['itemDescription']

    collection.insert_one({
        'name': item_name,
        'description': item_description
    })

    return jsonify({"status": "success", "message": "To-Do item added."})

# (Add your main run block if you have one)
# if __name__ == '__main__':
#     app.run(debug=True)