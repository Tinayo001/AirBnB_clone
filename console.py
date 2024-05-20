#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF (Ctrl+D) to exit the program
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on empty line + ENTER
        """
        pass

    def do_help(self, arg):
        """
        Help command to display available commands and their descriptions
        """
        cmd.Cmd.do_help(self, arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
