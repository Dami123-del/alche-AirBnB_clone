# AirBnB Clone - The Console

## Description

This project is the first step towards building a full web application: a
simple clone of [AirBnB](https://www.airbnb.com/). Everything built here is
reused by the later stages of the project (HTML/CSS templating, database
storage, a RESTful API and front-end integration).

In this first step we build:

- A parent class, `BaseModel`, that handles the initialization,
  serialization and deserialization of all future instances.
- A simple serialization/deserialization flow:
  **Instance <-> Dictionary <-> JSON string <-> file**
- All the classes used by the AirBnB application, each inheriting from
  `BaseModel`: `User`, `State`, `City`, `Amenity`, `Place` and `Review`.
- The first abstracted storage engine of the project: **File storage**
  (objects are saved to and loaded from a JSON file).
- Unit tests that validate every class and the storage engine.

## The Command Interpreter

The command interpreter is a small shell, built with Python's `cmd` module,
that is limited to one use-case: managing the objects of the project. With it
you can:

- Create a new object (e.g. a new `User` or a new `Place`)
- Retrieve an object from a file, a database, etc.
- Do operations on objects (count, compute stats, etc.)
- Update the attributes of an object
- Destroy an object

### How to start it

Clone the repository and run the console from the root of the project:

```
$ git clone https://github.com/<your-username>/AirBnB_clone.git
$ cd AirBnB_clone
$ ./console.py
```

If the file is not executable, make it so first with `chmod +x console.py`.

### How to use it

The console works in two modes.

**Interactive mode** - type commands at the `(hbnb)` prompt:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb) quit
$
```

**Non-interactive mode** - pipe commands into the console:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

### Commands

| Command   | Usage                                               | Description                                        |
|-----------|-----------------------------------------------------|----------------------------------------------------|
| `help`    | `help` or `help <command>`                          | Lists the available commands or describes one.     |
| `quit`    | `quit`                                              | Exits the console.                                 |
| `EOF`     | `Ctrl+D`                                            | Exits the console.                                 |
| `create`  | `create <class>`                                    | Creates a new instance, saves it and prints its id. |
| `show`    | `show <class> <id>`                                 | Prints the string representation of an instance.   |
| `destroy` | `destroy <class> <id>`                              | Deletes an instance and saves the change.          |
| `all`     | `all` or `all <class>`                              | Prints all instances, or all of one class.         |
| `update`  | `update <class> <id> <attribute> "<value>"`         | Adds or updates an attribute and saves the change. |

Valid classes: `BaseModel`, `User`, `State`, `City`, `Amenity`, `Place`,
`Review`.

### Examples

```
$ ./console.py
(hbnb) create User
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show User 49faff9a-6318-451f-87b6-910505c55907
[User] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2026, 11, 9, 18, 40, 12, 512930), 'updated_at': datetime.datetime(2026, 11, 9, 18, 40, 12, 512952)}
(hbnb) update User 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) all User
["[User] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2026, 11, 9, 18, 40, 12, 512930), 'updated_at': datetime.datetime(2026, 11, 9, 18, 41, 3, 103811), 'first_name': 'Betty'}"]
(hbnb) destroy User 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show User 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) create MyModel
** class doesn't exist **
(hbnb) quit
$
```

## Testing

All unit tests live in the `tests` folder, which mirrors the project layout
(e.g. `models/base_model.py` is tested in
`tests/test_models/test_base_model.py`).

Run all the tests:

```
$ python3 -m unittest discover tests
```

Run the tests of a single file:

```
$ python3 -m unittest tests/test_models/test_base_model.py
```

The tests also pass in non-interactive mode:

```
$ echo "python3 -m unittest discover tests" | bash
```

## Requirements

- Ubuntu 20.04 LTS
- Python 3.8.5
- Code style: pycodestyle 2.7.*

## Authors

See the [AUTHORS](./AUTHORS) file for the list of contributors.
