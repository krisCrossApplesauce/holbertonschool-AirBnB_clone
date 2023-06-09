#!/usr/bin/python3

class FileStorage:
    def __init__(self, *args, **kwargs):
        #if new instance add
        # a call to the method: new(self) on 'storage'
        self.__file_path = # stringpath to json file
        self.__objects = # store obj as <class name>.id

    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
        
    def save(self):
        # serializes __objects to json filepath if it exists
    
    def reload(save):
        #deseriealizes the json file to __objects if it exists
