import argparse

def create_parser():
    """ Creates the argument parser """

    # Main parser
    parser = argparse.ArgumentParser(
        prog="Task Tracker",
        description="A CLI application built in Python",
        formatter_class = argparse.ArgumentDefaultsHelpFormatter,
        epilog="When stuck, refer to this guide!"
    )

    # Actions
    actions = [
        "add",
        "update",
        "delete",
        "mark-in-progress",
        "mark-done",
        "list"
    ]

    # Subparsers
    subparsers = parser.add_subparsers(dest="action", help="Available actions")

    # Add a task
    add_task_subparser = subparsers.add_parser("add", help="Add a new task.")
    add_task_subparser.add_argument("description", type=str, help="Task description")

    # Update a task
    update_task_subparser = subparsers.add_parser("update", help="Update an existing task.")
    update_task_supbarser.add_argument("id", type=int, help="Task id")
    update_task_subparser.add_argument("description", type=str, help="Task description")

    # Delete a task
    delete_task_subparser = subparsers.add_parser("delete", help="Delete an existing task.")
    delete_task_subparser = subparsers.add_argument("id", type=int, help="Task id")

    # Mark a task as in progress
    in_progress_subparser = subparsers.add_parser("mark-in-progress", help="Mark a task as in progress.")

    # Mark a task as done
    task_done_subparser = subparsers.add_parser("mark-done", help="Mark a task as done.")

    # Listing tasks
    list_subparser = subparsers.add_parser("list", help="List all tasks.")
    list_subparser.add_argument("status", help="The task status.")

    return parser