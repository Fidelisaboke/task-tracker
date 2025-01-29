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
    tasks = get_data(TASKS_FILE)
        
    # Set the current index
    curr_index = 1
    if len(tasks) > 0:
        curr_index = len(tasks) + 1

    # Create a new task
    task = Task(curr_index, args.description)
    task = vars(task)
    tasks.append(task)
    
    save_data(TASKS_FILE, tasks)
    print(f"Task added successfully (ID: {task['id']})")


# Update an existing task
elif args.action == "update":
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

    save_data(TASKS_FILE, tasks)
    print("Task updated successfully.")


# Delete a specific task
elif args.action == "delete":
    tasks = get_data(TASKS_FILE)

    for task in tasks:
        # Remove task  if it exists
        if task['id'] == args.id:
            tasks.remove(task)
            break
    
    save_data(TASKS_FILE, tasks)
    print("Task removed successfully.")


# Mark a task as in progress or done
elif args.action == "mark-in-progress" or args.action == 'mark-done':
    tasks = get_data(TASKS_FILE)

    for task in tasks:
        if task['id'] == args.id and args.action == 'mark-in-progress':
            task['status'] = "in-progress"
            break
        elif task['id'] == args.id and args.action == 'mark-done':
            task['status'] = 'done'
            break
    else:
        print(f"Task does not exist (ID: {args.id})")
        raise SystemExit(1)

    save_data(TASKS_FILE, tasks)
    print("Task updated successfully.")

