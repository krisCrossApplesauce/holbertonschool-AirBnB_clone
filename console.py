#!/usr/bin/python3
""" console """
import cmd


class HBNBCommand(cmd.Cmd):
    """ console """
    prompt = '(hbnb)'

    def do_hello(self, line):
        """Prints a greeting message"""
        print("Hello, world!")

    def do_quit(self, line):
        """Exits the shell"""
        return True

    # Override emptyline() to avoid repeating the last command
    def emptyline(self):
        pass

    # def quit and EOF

    # def help

    # def create

    # def show

    # def destroy

    # all

    # update

if __name__ == '__main__':
    HBNBCommand().cmdloop()
