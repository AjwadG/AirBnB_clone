#!/usr/bin/python3
''' HBNBCommand class module'''
import cmd
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

models = {"BaseModel": BaseModel, "User": User, "State": State,
          "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    ''' cmd for AirBnB clone '''
    prompt = '(hbnb) '

    def default(self, line):
        '''when the command prefix is not recognized'''
        if '.' not in line or '(' not in line or ')' not in line:
            cmd.Cmd.default(self, line)
            return
        clas = line.split('.')[0]
        comand = line.split('.')[1].split('(')[0]
        args = line.split('(')[1].split(')')[0]
        args = args.split(',')
        if len(args) >= 2 and args[1].strip()[0] == '{':
            args = [args[0], ','.join(args[1:])]
        comands = {"all": self.do_all, "count": self.do_count,
                   "show": self.do_show,
                   "destroy": self.do_destroy, "update": self.do_update}
        if comand in comands:
            comands[comand](clas + ' ' + ' '.join(args))
        else:
            cmd.Cmd.default(self, line)

    def do_count(self, line):
        '''prints the count of the obj'''
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models:
            print("** class doesn't exist **")
        else:
            objs = storage.all()
            count = 0
            for key in objs:
                if args[0] == key.split('.')[0]:
                    count += 1
            print(count)

    def do_create(self, line):
        '''Creates a new instance of class'''
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models:
            print("** class doesn't exist **")
        else:
            new = models[args[0]]()
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
        elif args[0] not in models:
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
        elif args[0] not in models:
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
            if args[0] not in models:
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

    def update(self, inst, args):
        '''if update got adict passed to'''
        for i in range(0, len(args), 2):
            if (i + 1 == len(args)):
                return
            args[i] = args[i].strip("{:").strip('\'\"')
            args[i + 1] = args[i + 1].strip("},").strip('\"\'')
            args[i + 1] = args[i + 1].strip("\"\'")
            if args[i] in inst.__dict__:
                args[i + 1] = type(inst.__dict__[args[i]])(args[i + 1])
            inst.__dict__[args[i]] = args[i + 1]

    def do_update(self, line):
        '''Updates an instance based on the class name and id'''
        args = line.split()
        dic = False
        if len(args) > 3 and args[2].strip()[0] == '{':
            dic = True
        objs = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models:
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
            if not dic:
                args[3] = args[3].strip("\"\'")
                if args[2] in inst.__dict__:
                    args[3] = type(inst.__dict__[args[2]])(args[3])
                inst.__dict__[args[2]] = args[3]
            else:
                self.update(inst, args[2:])
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
