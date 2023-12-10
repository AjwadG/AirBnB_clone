#!/usr/bin/python3
""" Unittest for console """
import unittest
from io import StringIO
from unittest.mock import patch
import os
from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage


clases = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]


class ConsoleTests(unittest.TestCase):
    """Unittests for Console"""
    def setUp(self):
        '''deletes file.json before every test'''
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_base_and_empty_line(self):
        """check prombt and new line EOF and QUIT"""
        self.assertEqual(HBNBCommand.prompt, "(hbnb) ")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_wrong_comand(self):
        '''test for wrong comand'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("a"))
            self.assertEqual("*** Unknown syntax: a", f.getvalue().strip())

    def test_help_quistion_mark(self):
        '''test for wrong comand'''
        expected = '''Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(expected, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("?"))
            self.assertEqual(expected, f.getvalue().strip())

    def test_help_create(self):
        '''test for help and ? create output'''
        expected = '''Creates a new instance of a Class,
saves it to the JSON file) and prints the id.
Usage: Create <className>'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(expected, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("? create"))
            self.assertEqual(expected, f.getvalue().strip())

    def test_help_show(self):
        '''test for help and ? show output'''
        expected = '''Prints the string representation of instance
based on the class name and id.
Usage: show <className> <id>'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(expected, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("? show"))
            self.assertEqual(expected, f.getvalue().strip())

    def test_help_destroy(self):
        '''test for help and ? create output'''
        expected = '''Deletes an instance based on the class name and id,
(saves the change into the JSON file).
Usage: destroy <className> <id>'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(expected, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("? destroy"))
            self.assertEqual(expected, f.getvalue().strip())

    def test_help_all(self):
        '''test for help and ? create output'''
        expected = '''Prints all string representation of all instances
based or not on the class name.
Usage: all <className> OR all'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(expected, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("? all"))
            self.assertEqual(expected, f.getvalue().strip())

    def test_help_update(self):
        '''test for help and ? create output'''
        expected = '''Updates an instance based on the class name and id
adding or updating attribute (saves changes to JSON file)
Usage: update <class name> <id> <att name> "<att value>"'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(expected, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("? update"))
            self.assertEqual(expected, f.getvalue().strip())

    def test_help_quit(self):
        '''test for help and ? create output'''
        expected = '''Quit command to exit the program'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(expected, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("? quit"))
            self.assertEqual(expected, f.getvalue().strip())

    def test_help_EOF(self):
        '''test for help and ? create output'''
        expected = '''Quit when end of file'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(expected, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("? EOF"))
            self.assertEqual(expected, f.getvalue().strip())

    def test_create_wrong(self):
        '''test for wrong create use'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual("** class name missing **", f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create a"))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_show_wrong(self):
        '''test for wrong show use'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual("** class name missing **", f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show a"))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())
        for clas in clases:
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"show {clas}"))
                expected = "** instance id missing **"
                self.assertEqual(expected, f.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"show {clas} 000"))
                expected = "** no instance found **"
                self.assertEqual(expected, f.getvalue().strip())

    def test_show_dot_wrong(self):
        '''test for wrong .show use'''
        for clas in clases:
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"{clas}.show()"))
                expected = "** instance id missing **"
                self.assertEqual(expected, f.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"{clas}.show(000)"))
                expected = "** no instance found **"
                self.assertEqual(expected, f.getvalue().strip())

    def test_destroy_wrong(self):
        '''test for wrong destroy use'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual("** class name missing **", f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy a"))
            expected = "** class doesn't exist **"
            self.assertEqual(expected, f.getvalue().strip())
        for clas in clases:
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"destroy {clas}"))
                expected = "** instance id missing **"
                self.assertEqual(expected, f.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"destroy {clas} 000"))
                expected = "** no instance found **"
                self.assertEqual(expected, f.getvalue().strip())

    def test_destroy_dot_wrong(self):
        '''test for wrong .destroy use'''
        for clas in clases:
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"{clas}.destroy()"))
                expected = "** instance id missing **"
                self.assertEqual(expected, f.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"{clas}.destroy(000)"))
                expected = "** no instance found **"
                self.assertEqual(expected, f.getvalue().strip())

    def test_all_wrong(self):
        '''test for wrong all use'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all a"))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_update_wrong(self):
        '''test for wrong update use'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual("** class name missing **", f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update a"))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())
        for clas in clases:
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd("update Place"))
                expected = "** instance id missing **"
                self.assertEqual(expected, f.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"create {clas}"))
                PID = f.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as f:
                comand = f"update {clas} {reversed(PID)}"
                self.assertFalse(HBNBCommand().onecmd(comand))
                expected = "** no instance found **"
                self.assertEqual(expected, f.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"update {clas} {PID}"))
                out = f.getvalue().strip()
                expected = "** attribute name missing **"
                self.assertEqual(expected, out)
            with patch('sys.stdout', new=StringIO()) as f:
                comand = f"update {clas} {PID} water"
                self.assertFalse(HBNBCommand().onecmd(comand))
                expected = "** value missing **"
                self.assertEqual(expected, f.getvalue().strip())

    def test_update_dot_wrong(self):
        '''test for wrong .update use'''
        for clas in clases:
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"{clas}.update()"))
                expected = "** instance id missing **"
                self.assertEqual(expected, f.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"create {clas}"))
                PID = f.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as f:
                comand = f"{clas}.update({reversed(PID)})"
                self.assertFalse(HBNBCommand().onecmd(comand))
                expected = "** no instance found **"
                self.assertEqual(expected, f.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"{clas}.update({PID})"))
                out = f.getvalue().strip()
                expected = "** attribute name missing **"
                self.assertEqual(expected, out)
            with patch('sys.stdout', new=StringIO()) as f:
                comand = f"{clas}.update({PID}, water)"
                self.assertFalse(HBNBCommand().onecmd(comand))
                expected = "** value missing **"
                self.assertEqual(expected, f.getvalue().strip())

    def test_create_succes(self):
        '''test of using create successfuly'''
        expected = ""
        for clas in clases:
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd("create " + clas))
                output = f.getvalue().strip()
                self.assertNotEqual(expected, output)
                self.assertIn(f"{clas}.{output}", storage.all())

    def test_show_success(self):
        '''test of using show successfuly'''
        for clas in clases:
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"create {clas}"))
                PID = f.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"show {clas} {PID}"))
                output = f.getvalue().strip()
                expected = str(storage.all()[f"{clas}.{PID}"])
                self.assertEqual(expected, output)

    def test_show_success_dot(self):
        '''test of using .show successfuly'''
        for clas in clases:
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"create {clas}"))
                PID = f.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"{clas}.show({PID})"))
                output = f.getvalue().strip()
                expected = str(storage.all()[f"{clas}.{PID}"])
                self.assertEqual(expected, output)

    def test_destroy_success(self):
        '''test of using destroy successfuly'''
        for clas in clases:
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"create {clas}"))
                PID = f.getvalue().strip()
                self.assertIn(f"{clas}.{PID}", storage.all())
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"destroy {clas} {PID}"))
                output = f.getvalue().strip()
                expected = ""
                self.assertEqual(expected, output)
                self.assertNotIn(f"{clas}.{PID}", storage.all())

    def test_destroy_success_dot(self):
        '''test of using .destroy successfuly'''
        for clas in clases:
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"create {clas}"))
                PID = f.getvalue().strip()
            self.assertIn(f"{clas}.{PID}", storage.all())
            with patch('sys.stdout', new=StringIO()) as f:
                comand = f"{clas}.destroy({PID})"
                self.assertFalse(HBNBCommand().onecmd(comand))
                output = f.getvalue().strip()
                expected = ""
                self.assertEqual(expected, output)
                self.assertNotIn(f"{clas}.{PID}", storage.all())

    def test_all_success(self):
        '''test of using all successfuly'''
        all_expected = []
        for clas in clases:
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"create {clas}"))
                PID = f.getvalue().strip()
                self.assertIn(f"{clas}.{PID}", storage.all())
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"all {clas}"))
                output = f.getvalue().strip()
                expected = str(storage.all()[f"{clas}.{PID}"])
                all_expected.append(expected)
                self.assertEqual(str([expected]), output)
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(f"all"))
            output = f.getvalue().strip()
            for a in all_expected:
                self.assertIn(a, output)

    def test_all_success_dot(self):
        '''test of using .all successfuly'''
        for clas in clases:
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"create {clas}"))
                PID = f.getvalue().strip()
            self.assertIn(f"{clas}.{PID}", storage.all())
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"{clas}.all()"))
                output = f.getvalue().strip()
                expected = str(storage.all()[f"{clas}.{PID}"])
                self.assertEqual(str([expected]), output)

    def test_update_success(self):
        '''test of using update successfuly'''
        expected = ""
        for clas in clases:
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"create {clas}"))
                PID = f.getvalue().strip()
                obj = storage.all()[f"{clas}.{PID}"]
            self.assertFalse(hasattr(obj, "what's"))

            with patch('sys.stdout', new=StringIO()) as f:
                comand = f"update {clas} {PID} what's \"your\""
                self.assertFalse(HBNBCommand().onecmd(comand))
                output = f.getvalue().strip()
                self.assertEqual(expected, output)
            self.assertEqual(obj.__dict__["what's"], "your")

            with patch('sys.stdout', new=StringIO()) as f:
                comand = f"update {clas} {PID} what's \"NAME\""
                self.assertFalse(HBNBCommand().onecmd(comand))
                output = f.getvalue().strip()
                self.assertEqual(expected, output)
            self.assertEqual(obj.__dict__["what's"], "NAME")

    def test_update_dot_success(self):
        '''test of using .update successfuly'''
        expected = ""
        for clas in clases:
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"create {clas}"))
                PID = f.getvalue().strip()
                obj = storage.all()[f"{clas}.{PID}"]
            self.assertFalse(hasattr(obj, "Tony"))
            self.assertFalse(hasattr(obj, "Ezekiel"))

            with patch('sys.stdout', new=StringIO()) as f:
                comand = f"{clas}.update({PID}, " + "{\"Tony\": \"Tony\"})"
                self.assertFalse(HBNBCommand().onecmd(comand))
                output = f.getvalue().strip()
                self.assertEqual(expected, output)
                self.assertEqual(obj.__dict__["Tony"], "Tony")

            with patch('sys.stdout', new=StringIO()) as f:
                comand = f"{clas}.update({PID}, " + "{\"Tony\": \"Fyou\"})"
                self.assertFalse(HBNBCommand().onecmd(comand))
                output = f.getvalue().strip()
                self.assertEqual(expected, output)
                self.assertEqual(obj.__dict__["Tony"], "Fyou")
                self.assertEqual(type(getattr(obj, "Tony")), str)

            with patch('sys.stdout', new=StringIO()) as f:
                comand = f"{clas}.update({PID}, Ezekiel, \"Ezekiel\")"
                self.assertFalse(HBNBCommand().onecmd(comand))
                output = f.getvalue().strip()
                self.assertEqual(expected, output)
                self.assertEqual(obj.__dict__["Ezekiel"], "Ezekiel")

            with patch('sys.stdout', new=StringIO()) as f:
                comand = f"{clas}.update({PID}, Ezekiel, \"Fyou\")"
                self.assertFalse(HBNBCommand().onecmd(comand))
                output = f.getvalue().strip()
                self.assertEqual(expected, output)
                self.assertEqual(obj.__dict__["Ezekiel"], "Fyou")
                self.assertEqual(type(getattr(obj, "Ezekiel")), str)

    def test_count_success_dot(self):
        '''test of using .count successfuly'''
        for clas in clases:
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"create {clas}"))
                PID = f.getvalue().strip()
            self.assertIn(f"{clas}.{PID}", storage.all())
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd(f"{clas}.count()"))
                output = f.getvalue().strip()
                self.assertEqual("1", output)


if __name__ == "__main__":
    unittest.main()
