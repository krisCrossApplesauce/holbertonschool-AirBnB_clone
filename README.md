# Air BnB - Holberton
This repo contains the following for an Air BnB clone project:

## Description
This repo aims to act as a clone build of the web application AirBnB that aims to mimic its command interpretation functionality. The command line can be used to manage data saved to a json file storage system.

## Instructions for Use
* Clone this repo from github and Install Python3 if not currently installed
* Open python terminal and navigate to this projects directory
* run './console.py', or, python3 console.py

## Command Line Interpreter with the following Requisites and Functionalities
* Built upon the CMD module
* Create a new instance of BaseModel and save it to JSON and prints the ID
* Retrieve data from a database
* Operate on objects individually using commands
* Destroy an instance based on the class name and ID
* Update an instance based on the class name and ID by adding or updating attribute
* Print a string representation of an instance based on the class name and ID
* Save all user-made changes into a JSON file


## Use Case Examples
* the entry point for the program is console.py
```bash
Apple&Gum_AirBnB_clone$./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all
-
["[BaseModel] (0eb4d19f-e54e-40fc-9ed8-74a72c468f54) {'id': '0eb4d19f-e54e-40fc-9ed8-74a72c468f54', 'created_at': datetime.datetime(2023, 6, 13, 18, 51, 13, 445268), 'updated_at': datetime.datetime(2023, 6, 13, 18, 51, 13, 445283)}", "[User] (92c8391f-1a16-4f7a-9818-e94cafa23c2b) {'id': '92c8391f-1a16-4f7a-9818-e94cafa23c2b', 'created_at': datetime.datetime(2023, 6, 13, 18, 51, 16, 139695), 'updated_at': datetime.datetime(2023, 6, 13, 18, 51, 16, 139715)}", "[City] (59872cd1-0692-40a2-8bd8-65184643a1fd) {'id': '59872cd1-0692-40a2-8bd8-65184643a1fd', 'created_at': datetime.datetime(2023, 6, 13, 18, 51, 18, 575985), 'updated_at': datetime.datetime(2023, 6, 13, 18, 51, 18, 575999)}", "[Place] (ae50374c-3e75-4e7d-b120-13711cca53a8) {'id': 'ae50374c-3e75-4e7d-b120-13711cca53a8', 'created_at': datetime.datetime(2023, 6, 13, 18, 51, 21, 143996), 'updated_at': datetime.datetime(2023, 6, 13, 18, 51, 21, 144011)}", "[State] (92a677f3-fd9f-4993-9f9b-823f490bff13) {'id': '92a677f3-fd9f-4993-9f9b-823f490bff13', 'created_at': datetime.datetime(2023, 6, 13, 18, 51, 24, 369156), 'updated_at': datetime.datetime(2023, 6, 13, 18, 51, 24, 369170)}", "[Amenity] (8f7ab8c0-bff4-4dc1-b59a-81907ca7fe4a) {'id': '8f7ab8c0-bff4-4dc1-b59a-81907ca7fe4a', 'created_at': datetime.datetime(2023, 6, 13, 18, 51, 27, 317225), 'updated_at': datetime.datetime(2023, 6, 13, 18, 51, 27, 317242)}"]
-
(hbnb) quit
```

## Authors
* Evan Parker Newman-Chock -- <gumquat@gmail.com>
* Karis Rachel Richardson -- <karisrr2203@gmail.com>


## CMD Flowchart
![flowchart gumapple](https://github.com/krisCrossApplesauce/holbertonschool-AirBnB_clone/assets/23125776/6615bb64-22da-4b74-8cbc-6c1ceabd3670)
![flowchart_marker](https://github.com/krisCrossApplesauce/holbertonschool-AirBnB_clone/assets/23125776/a216f68a-3843-4321-9d05-5831d893de42)

Flow and Capability of the Program:
* Create instances of an object at the users discretion, inheriting from any needed classes and creating a uuid for the instance
* Manipulate data within loaded object instances, or delete the instance
* Serialize an object instance into a json file for convenient storage
* De-Serialize a json file (re-load saved object instances), openening it 
* Manipulate data again, rinse and repeat above steps as needed




