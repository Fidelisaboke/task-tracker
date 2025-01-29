""" Main program """

import os
import logging
import json
from functions import create_parser, get_data, save_data
from task import Task
from datetime import datetime

# Tasks file
TASKS_FILE = "tasks.json"

# Parse command line arguments
parser = create_parser()
args = parser.parse_args()

match args.action:
    # Add a new task
    case "add":
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
    case "update":
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

        
    # Delete a task
    case "delete":
        tasks = get_data(TASKS_FILE)

        for task in tasks:
            # Remove task if it exists
            if task['id'] == args.id:
                tasks.remove(task)
                break
        
        save_data(TASKS_FILE, tasks)
        print("Task removed successfully.")


    # Mark a task as in progress or done
    case "mark-in-progress" | 'mark-done':
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


    # List tasks
    case "list":
        tasks = get_data(TASKS_FILE)
        match args.status:
            case "done":
                tasks = json.dumps([
                    task for task in tasks if task['status'] == 'done'
                ], indent=4)

            case "to-do":
                tasks = json.dumps([
                    task for task in tasks if task['status'] == 'to-do'
                ], indent=4)

            case "in-progress":
                tasks = json.dumps([
                    task for task in tasks if task['status'] == 'in-progress'
                ], indent=4)

            case _:
                tasks = json.dumps(tasks, indent=4)

        print(tasks)

