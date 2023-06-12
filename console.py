#!/usr/bin/python3
""" console """
import cmd


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
        if line is not None and line != "":
            args = line.split()
        else:
            print("** class name missing **")

    def do_all(self, line):
        pass

    # def update

if __name__ == '__main__':
    HBNBCommand().cmdloop()
