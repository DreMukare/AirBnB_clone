#!/usr/bin/python3
"""
    contains entry point of command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
        class HBNBCommand
    """
    def __init__(self):
        """
            prompts user
        """
        cmd.Cmd.__init__(self)
        self.prompt = '(hnbn)'

    def help_quit(self):
        """
            handling help command
        """
        print('Quit command to exit the program')

    def emptyline(self):
        """
            Called when an empty line is entered
            in response to the prompt.

            If this method is not overridden,
            it repeats the last nonempty
            command entered.
        """
        pass

    def do_quit(self, arg):
        """
            quits the cli
        """
        raise SystemExit

    def do_EOF(self, arg):
        """
            handles EOF
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
