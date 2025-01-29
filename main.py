""" Main program """

import os
import logging
from functions import create_parser, get_data, save_data
from task import Task
from datetime import datetime

# Tasks file
TASKS_FILE = "tasks.json"

# Parse command line arguments
parser = create_parser()
args = parser.parse_args()


# Add a new task.
if args.action == "add":
    # Get tasks frm the task file
    tasks = get_data(TASKS_FILE)
        
    # Set the current index
    curr_index = 1
    if len(tasks) > 0:
        curr_index = len(tasks) + 1

    # Create a new task
    task = Task(curr_index, args.description)
    task = vars(task)
    tasks.append(task)
    
    # Save the tasks to the tasks file
    save_data(TASKS_FILE, tasks)
    print(f"Task added successfully (ID: {task['id']})")


# Update an existing task
elif args.action == "update":
    # Get tasks from the tasks file
    tasks = get_data(TASKS_FILE)  

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
    save_data(TASKS_FILE, tasks)
    print("Task updated successfully.")

elif args.action == "delete":
    # Get tasks from tasks file
    tasks = get_data(TASKS_FILE)

    for task in tasks:
        # Remove task  if it exists
        if task['id'] == args.id:
            tasks.remove(task)
            break
    
    save_data(TASKS_FILE, tasks)
    print("Task removed successfully.")