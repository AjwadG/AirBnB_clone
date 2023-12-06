#!/usr/bin/python3
''' HBNBCommand class module'''
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    ''' cmd for AirBnB clone '''
    prompt = '(hbnb) '

    def do_create(self, line):
        '''Creates a new instance of class'''
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            storage.save()
            print(new.id)

    def help_create(self):
        '''prints crate's help'''
        print("Creates a new instance of a Class,")
        print("saves it to the JSON file) and prints the id.")
        print("Usage: Create <className>\n")

    def do_show(self, line):
        '''Prints the string representation of an instance'''
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objs:
                print(objs[key])
            else:
                print("** no instance found **")

    def help_show(self):
        '''prints show's help'''
        print("Prints the string representation of instance")
        print("based on the class name and id.")
        print("Usage: show <className> <id>\n")

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objs:
                del objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def help_destroy(self):
        '''prints destroy's help'''
        print("Deletes an instance based on the class name and id,")
        print("(saves the change into the JSON file).")
        print("Usage: destroy <className> <id>\n")

    def do_all(self, line):
        '''Prints all string representation of all instances'''
        args = line.split()
        objs = storage.all()
        strs = []
        if len(args) != 0:
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
                return
            else:
                for key in objs:
                    if objs[key].__class__.__name__ == args[0]:
                        strs.append(str(objs[key]))
        else:
            for key in objs:
                strs.append(str(objs[key]))
        print(strs)

    def help_all(self):
        '''prints all's help'''
        print("Prints all string representation of all instances")
        print("based or not on the class name.")
        print("Usage: all <className> OR all\n")

    def do_update(self, line):
        '''Updates an instance based on the class name and id'''
        args = line.split()
        objs = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in objs:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            inst = objs[f"{args[0]}.{args[1]}"]
            args[3] = args[3].strip("\"")
            if args[2] in inst.__dict__:
                args[3] = type(inst.__dict__[args[2]])(args[3])
            inst.__dict__[args[2]] = args[3]
            inst.save()
            storage.save()

    def help_update(self):
        '''prints update's help'''
        print("Updates an instance based on the class name and id")
        print("adding or updating attribute (saves changes to JSON file)")
        print("Usage: update <class name> <id> <att name> \"<att value>\"\n")

    def do_quit(self, line):
        '''Quit command to exit the program\n'''
        return True

    def emptyline(self):
        '''called when nothing is entered'''
        print

    def do_EOF(self, line):
        '''Quit when end of file'''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
