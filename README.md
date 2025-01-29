# Task Tracker CLI
This is a CLI application that managers tasks. It makes use of a JSON file to store and manage the tasks through commands entered in the CLI.

## Table of Contents
1. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
2. [Usage](#usage)
    - [Help Message](#help-message)
    - [Add Task](#add-task)
    - [Update Task](#update-task)
    - [Delete Task](#delete-task)
    - [Update Task Status](#update-task-status)
    - [Listing Tasks](#listing-tasks)
3. [Acknowledgements](#acknowledgements)

## Getting Started
### Prerequisites
- Python 3.10 or higher

### Installation
1. Clone the repository:
```bash
git clone https://github.com/Fidelisaboke/task-tracker.git
```

2. Navigate to the project directory:
```bash
cd task-tracker
```

## Usage
#### Help Message
- Display the help message:
```bash
python3 main.py --help
```
**Note**: The `--help` or `-h` option can also be used with the existing subcommands for more information on how to use them.

#### Add Task
- To add a new task, use the `add` command followed by a **description** of the task as an argument. For instance:
```bash
python3 main.py add "Example Task"
```
**Note:** Refer to the `tasks.json` file created to see the task.

#### Update Task
- To update an existing task, use the `update` command with the **id** of the task to be updated, followed by the new **description** for the task:
```bash
python3 main.py update 1 "Example New Task"
```

#### Delete Task 
- To delete a task, use the `delete` command, followed by the **id** of the task to be removed:
```bash
python3 main.py delete 1
```

#### Update Task Status
- To mark a task as `in-progress`, use the `mark-in-progress` command followed by the **id** of the task to be updated:
```bash
python3 main.py mark-in-progress 1
```

- Similarly, to mark a task as `done`, use the `mark-done` command followed by the **id** of the task:
```bash
python3 main.py mark-done 1
```

#### Listing Tasks
- List all tasks:
```bash
python3 main.py list
```

- List `to-do` tasks:
```bash
python3 main.py list todo
```

- List tasks `in-progress`:
```bash
python3 main.py list in-progress
```

- List `done` tasks:
```bash
python3 main.py list done
```

## Acknowledgements
I would like to appreciate the creators of the following resources:
- [Roadmap.sh - Task Tracker](https://roadmap.sh/projects/task-tracker): For information on the Task Tracker CLI project.