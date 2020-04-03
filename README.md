# HBNB_CLONE_V2

This is the console /command interpreter for the Holberton School Airbnb clone V2 project. The console can be used to store objects in and retrieve objects from a JSON.

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
