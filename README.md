# 0x00. AirBnB clone - The console

## Description
The AirBnB clone project is a project to build a clone of the AirBnB website, step by step learning the real
life implementation of complex websites such as the AirBnB website and developint the necessary skills towards
building a full web application. This first step is very important and will be built upon subsequently in following projects such as: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help:

1. put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
2. create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
3. create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
4. create the first abstracted storage engine of the project: File storage.
5. create all unittests to validate all our classes and storage engine

## Command Interpreter

The command interpreter, often referred to as a shell, allows users to interact with the system by typing commands. It interprets these commands and facilitates the execution of corresponding operations. In this project, the command interpreter provides a set of commands and functionalities to perform common tasks efficiently. These commands will:

1. Create a new object (ex: a new User or a new Place)
2. Retrieve an object from a file, a database etc…
3. Do operations on objects (count, compute stats, etc…)
4. Update attributes of an object
5. Destroy an object

## How to Start

To start the command interpreter, follow these steps:

1. Clone the repository to your local machine:
```bash
git clone https://github.com/AjwadG/AirBnB_clone.git
```

2. Navigate to the project directory:
```bash
cd AirBnB_clone
```

3. Run the command interpreter:
```bash
./console.py
```
Ensure that you have Python installed on your system before running the interpreter.

## How to Use

Once the command interpreter is running, you can enter commands to perform various actions. The syntax for commands is as follows:

command [argument(s)]

Replace `command` with the specific command you want to execute, and include any necessary options or arguments.

## Examples

### Example 1: Create a new BaseModel

```bash
create BaseModel
```
Output:
```
c160b8a9-0398-475d-aa32-0ff5f419ac0c
```

### Example 2: Show a created BaseModel

```bash
show BaseModel c160b8a9-0398-475d-aa32-0ff5f419ac0c
```

Output:
```
[BaseModel] (c160b8a9-0398-475d-aa32-0ff5f419ac0c) {'created_at': datetime.datetime(2023, 12, 6, 8, 10, 25, 903293), 'id': 'c160b8a9-0398-475d-aa32-0ff5f419ac0c', 'updated_at': datetime.datetime(2023, 12, 6, 8, 10, 25, 903300)}
```

### Example 3: Destroy a BaseModel

```bash
destroy BaseModel c160b8a9-0398-475d-aa32-0ff5f419ac0c
```

### Example 4: Quitting the console

```bash
quit
```

These are just some basic examples, and the command interpreter supports a variety of commands and options. Refer to the documentation or use the `--help` option with a specific command to get more information.

Feel free to explore the available commands and experiment with different options to suit your needs.

