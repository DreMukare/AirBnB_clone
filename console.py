#!/usr/bin/python3
"""
    contains entry point of command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User

class HBNBCommand(cmd.Cmd):
    """
        class HBNBCommand
    """
    all_classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                   'City': City, 'Amenity': Amenity, 'Place': Place,
                   'Review': Review}

    def __init__(self):
        """
            prompts user
        """
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '

    def do_create(self, name):
        """
            Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id
        """
        if not name:
            print("** class name missing **")
        if name not in storage.classes:
            print("** class doesn't exist **")
        else:
            instance = storage.classes[name]()
            instance.save()
            print(instance.id)

    def do_show(self, input):
        """
            prints string representation of an instance
        """
        vars = input.split(' ')
        if not input:
            print("** class name missing **")
            return
        elif vars[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(vars) < 2:
            print("** instance id missing **")
        else:
            key = '{}.{}'.format(vars[0], vars[1])
            if key not in storage.all():
                print('** no instance found **')
            else:
                print(storage.all()[key])

    def do_destroy(self, input):
        """
            Deletes an instance
        """
        vars = input.split(' ')
        if not input:
            print("** class name missing **")
        elif vars[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(vars) < 2:
            print("** instance id missing **")
        else:
            key = '{}.{}'.format(vars[0], vars[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, input):
        """
            prints string representations of all instances
        """
        if input not in storage.classes:
            print('** class does not exist **')
        else:
            output = [str(obj) for k, obj in storage.all().items()]
            print(output)

    def do_update(self, input):
        """
            updates instance based on class name and id
        """
        vars = input.split(' ')
        if not input:
            print("** class name missing **")
        elif vars[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(vars) < 2:
            print("** instance id missing **")
        else:
            key = '{}.{}'.format(vars[0], vars[1])
            if key not in storage.all():
                print("** no instance found **")
            if len(vars) < 3:
                print('** attribute name missing **')
            if len(vars) < 4:
                print('** value missing **')
            else:
                vars[3] = vars[3].strip("\"")
                storage.all()[key].__dict__[vars[2]] = vars[3]
                vars[0].save()
                storage.save()

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
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
