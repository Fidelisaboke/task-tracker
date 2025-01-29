""" Main program """

import os
import json
import logging
from functions import create_parser, get_data
from task import Task
from datetime import datetime

# Tasks file
TASKS_FILE = "tasks.json"

# Parse command line arguments
parser = create_parser()
args = parser.parse_args()


# Add a new task.
if args.action == "add":
    data = get_data(TASKS_FILE)
        
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


# Update an existing task
elif args.action == "update":
    tasks = get_data(TASKS_FILE)
    print(tasks)        

    for task in tasks:

        # Update task if it exists
        if task['id'] == args.id:
            task['description'] = args.description
            task['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break

    else:
        print(f"Task does not exist (ID: {args.id})")
        raise SystemExit(1)

    # Save the tasks to the tasks file
    with open(TASKS_FILE, "w") as file:
        tasks.append(task)
        serialized_tasks_data = json.dumps(tasks, indent=4)
        file.write(serialized_tasks_data)

        print("Task updated successfully.")

    
    

