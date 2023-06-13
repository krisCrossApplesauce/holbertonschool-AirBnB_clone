#!/usr/bin/python3
""" console """
import cmd
import os
import json
from models.models import models_dict
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import models


class HBNBCommand(cmd.Cmd):
    """ console """
    prompt = '(hbnb)'

    def do_hello(self, line):
        """Prints a greeting message"""
        print("Hello, world!")

    def do_quit(self, line):
        """Exits the shell ... EOF"""
        return True

    def do_EOF(self, line):
        """Exits the shell"""
        return True

    # Override emptyline() to avoid repeating the last command
    def emptyline(self):
        """empty line + 'enter' executes nothing"""
        pass

    # def help [this is autoincluded]

    def do_create(self, arg):
        """creates new inst of BaseModel saved to json file and prints ID"""
        if not arg:
            print("** class name missing **")
        elif arg not in models_dict.keys():
            print("** class doesn't exist **")
        else:
            new_model = models_dict[arg]()
            new_model.save()
            print(new_model.id)

    def do_show(self, arg):
        """print string rep of instance"""
        args = arg.split()
        class_name = args[0]
        instance_id = args[1]
        obj_dict = models.storage.all() # double check this!

        if not args:
            print("** class name missing **")
            return
        if class_name not in models_dict.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2: #this checks if id exists
            print("** instance id missing **")
            return
        key = (f"{class_name}.{instance_id}")
        if key not in obj_dict:
            print("** no instance found **")
            return
        print(obj_dict[key])

    def do_destroy(self, line):
        """ detroys given instance """
        if line is None or line == "":
            print("** class name missing **")
        else:
            args = line.split(" ")
            if args[0] not in models_dict.keys():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif f"{args[0]}.{args[1]}" not in models.storage.all():
                print("** no instance found **")
            else:
                with open("file.json", "w") as file:
                    models.storage.remove(f"{args[0]}.{args[1]}")
                pass

    def do_all(self, arg):
        """prints string rep of existing instances"""
        buff_list = []
        if arg not in models_dict.keys() and arg != "":
            print("** class doesn't exist **")
            return
        else:
            for obj in models.storage.all():
                if isinstance(obj, models_dict[arg]):
                    buff_list.append(str(obj))
        return buff_list

    # update

if __name__ == '__main__':
    HBNBCommand().cmdloop()
