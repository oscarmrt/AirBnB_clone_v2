# HBNB_CLONE_V2

The first segment of the AirBnB project at Holberton School is the console, in this project we are going to share all our knowledge about higher level programming. The goal is to eventually deploy our server a simple copy of AirBnB. A command interpreter is created in this segment to store objects in and retrieve objects from a JSON.

### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

### Installing

Step by step how to run HBNB

*First of all clone the repository* 
```
git clone "https://github.com/dgquintero/AirBnB_clone_v2.git"
```
*Go to the directory AirBnB_clone_v2*
```
cd AirBnB_clone_v2/
```
*Run it on interactive mode*
```
./console.py
```
*Run it non-interactively*
```
echo "<command>" | ./console.py
````

## Running the tests

The AirBnB_clone works like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

The AirBnB_clone works like this in non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
#### Create:
`create <class name>`
Ex:
`create BaseModel`

#### Show:
`show <class name> <object id>`
Ex:
`show User my_id`

#### Destroy:
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

#### All:
`all` or `all <class name>`
Ex:
`all` or `all State`

#### Quit:
`quit` or `EOF`

#### Help:
`help` or `help <command>`
Ex:
`help` or `help quit`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`

## Built With

* [Python](https://www.python.org) - Programming language.


## Authors
* **Oscar Rodriguez** - [Github](https://github.com/oscarmrt) - [Twitter](https://twitter.com/OscaRT07)
* **Daniel Quintero** - [Github](https://github.com/dgquintero) - [Twitter](https://twitter.com/danielq02)
* **David Ortiz** - [Github](https://github.com/daod2003) - [Twitter](https://twitter.com/alejoortizd)

## License

AirBnB_clone has an open source license [Open Source Definition](https://opensource.org/osd) — in brief, they allow software to be freely used, modified, and shared
