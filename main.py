""" Main program """

import os
import json
import logging
from functions import create_parser
from task import Task

# Tasks file
TASKS_FILE = "tasks.json"

# Create JSON file if not present
if not os.path.exists(TASKS_FILE):
    open(TASKS_FILE, "x").close()


# Parse command line arguments
parser = create_parser()
args = parser.parse_args()


# Add a new task.
if args.action == "add":

    # Check if any data exists
    with open(TASKS_FILE, "r") as file:
        if os.path.getsize(TASKS_FILE) > 0:
            data = json.load(file)
        else:
            data = []
        
    # Set the current index
    curr_index = 1
    if len(data) > 0:
        curr_index = len(data) + 1

    # Create a new task
    task = Task(curr_index, args.description)
    task = vars(task)
    
    # Save the tasks to the tasks file
    with open(TASKS_FILE, "w") as file:
        data.append(task)
        serialized_data = json.dumps(data, indent=4)
        file.write(serialized_data)

        print(f"Task added successfully (ID: {task['id']})")
