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
        obj_dict = models.storage.all()

        if not args:
            print("** class name missing **")
        elif args[0] not in models_dict.keys():
            print("** class doesn't exist **")
        elif len(args) < 2: #this checks if id exists
            print("** instance id missing **")
        else:
            key = (f"{args[0]}.{args[1]}")
            if key not in obj_dict:
                print("** no instance found **")
            print(obj_dict[key])

    def do_destroy(self, line):
        """ detroys given instance """
        if line is None or line == "":
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in models_dict.keys():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif f"{args[0]}.{args[1]}" not in models.storage.all():
                print("** no instance found **")
            else:
                models.storage.remove(f"{args[0]}.{args[1]}")

    def do_all(self, arg):
        """prints string rep of existing instances"""
        if arg not in models_dict.keys() or arg != "":
            print("** class doesn't exist **")
        else:
            print(models.storage.all())

    def do_update(self, arg):
        """UPDATES an inst class name and id"""
        args = arg.split()
        if not arg:
            print("** class name is missing **")
        if arg[0] not in models_dict:
            print("** class doesn't exists **")
        if not models.storage.all():
            print("** no instance found **")
        if len(args) < 2:
            print("** instance id missing **")
        if len(args) < 3:
            print("** attribute name missing **")
        if len(args) < 4:
            print("** value missing **")
        setattr(models.storage.all(), args[0], args[3])
        args[3].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
