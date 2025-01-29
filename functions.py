""" This module contains useful functions for the program. """

import argparse
import os
import json

def create_parser():
    """ Creates the argument parser. """

    # Main parser
    parser = argparse.ArgumentParser(
        prog="task-cli",
        description="A CLI application built in Python",
        formatter_class = argparse.ArgumentDefaultsHelpFormatter,
        epilog="When stuck, refer to this guide!"
    )

    # Subparsers
    subparsers = parser.add_subparsers(dest="action", help="Available actions")

    # Add a task
    add_task_subparser = subparsers.add_parser("add", help="Add a new task.")
    add_task_subparser.add_argument(
        "description", 
        type=str, 
        help="Task description"
    )

    # Update a task
    update_task_subparser = subparsers.add_parser(
        "update", 
        help="Update an existing task."
    )
    update_task_subparser.add_argument("id", type=int, help="Task id")
    update_task_subparser.add_argument(
        "description", 
        type=str, 
        help="Task description"
    )

    # Delete a task
    delete_task_subparser = subparsers.add_parser(
        "delete", 
        help="Delete an existing task."
    )
    delete_task_subparser.add_argument("id", type=int, help="Task id")

    # Mark a task as in progress
    in_progress_subparser = subparsers.add_parser(
        "mark-in-progress", 
        help="Mark a task as in progress."
    )
    in_progress_subparser.add_argument("id", type=int, help="Task id")

    # Mark a task as done
    task_done_subparser = subparsers.add_parser(
        "mark-done", 
        help="Mark a task as done."
    )
    task_done_subparser.add_argument("id", type=int, help="Task id")

    # Listing tasks
    list_subparser = subparsers.add_parser("list", help="List all tasks.")
    list_subparser.add_argument(
        "status", 
        help="The task status.", 
        nargs="?"
    )

    return parser


def get_data(filename):
    """ Gets data from file. """

    # Create JSON file if not present
    if not os.path.exists(filename):
        open(filename, "x").close()

    with open(filename, "r") as file:
        if os.path.getsize(filename) > 0:
            return json.load(file)
    
    return []


def save_data(filename, data):
    """ Saves data to the file. """

    with open(filename, "w") as file:
        serialized_data = json.dumps(data, indent=4)
        file.write(serialized_data)
    