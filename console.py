#!/usr/bin/python3
""" console """
import cmd
from models.models import models
import models


class HBNBCommand(cmd.Cmd):
    """ console """
    prompt = '(hbnb)'

    def do_hello(self, arg):
        """Prints a greeting message"""
        print("Hello, world!")

    def do_quit(self, arg):
        """Exits the shell"""
        return True

    def do_EOF(self, arg):
        """Exits the shell"""
        return True

    # Override emptyline() to avoid repeating the last command
    def emptyline(self):
        pass

    # def help

    # def create

    # def show

    def do_destroy(self, line):
        if line is None and line == "":
            print("** class name missing **")
        else:
            args = line.split(" ")
            if args[0] not in models:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif "{args[0]}.{args[1]}" not in models.storage.all():
                print("** no instance found **")
            else:
                # delete the instance
                pass

    # def all

    # def update

if __name__ == '__main__':
    HBNBCommand().cmdloop()
