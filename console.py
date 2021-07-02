#!/usr/bin/python3
"""
    contains entry point of command interpreter
"""
import cmd
import sys
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

    def do_create(self, line):
        """Creates a new BaseModel instance
        Args:
            None
        Prints id of the new BaseModel instance
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
        else:
            base1 = HBNBCommand.all_classes[line]()
            base1.save()
            print(base1.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name
        and id. Example: $ show BaseModel 1234-1234-1234.
        """
        a_list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif a_list[0] not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
            return
        elif len(a_list) == 1:
            print("** instance id missing **")
            return
        else:
            ke_y = a_list[0] + "." + a_list[1]
            all_instances = storage.all()
            if ke_y not in all_instances.keys():
                print("** no instance found **")
            else:
                obj = all_instances[ke_y]
                print(obj)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id. Example: (hbnb)  destroy BaseModel 1234-1234-1234.
        """
        a_list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif a_list[0] not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
            return
        elif len(a_list) == 1:
            print("** instance id missing **")
            return
        else:
            ke_y = a_list[0] + "." + a_list[1]
            all_instances = storage.all()
            if ke_y not in all_instances.keys():
                print("** no instance found **")
            else:
                del(all_instances[ke_y])
                storage.save()

    def do_all(self, line):
        """
        Prints the string representation of all instances
        Example: (hbnb) all BaseModel
        or (hbnb) all
        """
        obj_list = []
#        storage.reload()
        objs = storage.all()
        try:
            if len(line) != 0:
                eval(line)
            else:
                pass
        except NameError:
            print("** class doesn't exist **")
            return
        line.strip()
        for key, val in objs.items():
            if len(line) != 0:
                if type(val) is eval(line):
                    val = str(objs[key])
                    obj_list.append(val)
            else:
                val = str(objs[key])
                obj_list.append(val)
        print(obj_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file). Ex: (hbnb)
        update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com".
        """
        a_list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif a_list[0] not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
            return
        elif len(a_list) == 1:
            print("** instance id missing **")
            return
        elif len(a_list) == 2:
            print("** attribute name missing **")
        elif len(a_list) == 3:
            print("** value missing **")
        else:
            ke_y = a_list[0] + "." + a_list[1]
            all_instances = storage.all()
            if ke_y not in all_instances.keys():
                print("** no instance found **")
            else:
                obj = all_instances[ke_y]
                setattr(obj, a_list[2], a_list[3])
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

    def default(self, line):
        """enables cli to carry out differently formatted commands """
        all_classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
               'City': City, 'Amenity': Amenity, 'Place': Place,    
               'Review': Review}                                    
        cmds = line.split('.')
        objs = storage.all()
        obj_list = []
        count = 0 
        if cmds[0] in all_classes.keys():
            if cmds[1] == 'all()':
            # print all instances of class
                for k, v in objs.items():
                    if type(v) is eval(cmds[0]):
                        v = str(objs[k])
                        obj_list.append(v)
                print(obj_list)
            elif cmds[1] == 'count()':
            # print number of class instances
               for k, v in objs.items():
                   if type(v) is eval(cmds[0]):
                       count += 1
               print(count)
            id_sect = cmds[1].split('(')
            act_id = id_sect[1].replace(')', '')
            if act_id:
                if len(act_id) == 36:
                    key = cmds[0] + '.' + act_id
                    if id_sect[0] == 'show':
                        print(obj[key])
                    elif id_sect[0] == 'destroy':
                        del obj[key]
                elif len(act_id) > 36 and id_sect[0] == 'update':
                    more_args = act_id.split(', ')
                    id_str = more_args[0]
                    key = cmds[0] + '.' + id_str
                    dict_o = obj[key] 
                    if len(more_args) == 2 and more_args[1][0] == '{':
                        for k, v in more_args[1]:
                            dict_o[k] = v
                    else:
                        if len(more_args) == 2:
                            print('** value missing **')
                        elif len(more_args) == 3:
                            setattr(dict_o, more_args[1], more_args[2])
            else:
                print('** instance id missing **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
