#!/usr/bin/python3
"""test script for the Console module"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """The Test Class"""

    def setUp(self):
        "function to set up test class"
        self.console = HBNBCommand()

    def test_create(self):
        "testing the create function"
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Checking if ID length is 36

    def test_create_valid_object(self):
        "testing the create function"
        args = 'create BaseModel my_attr=123 my_str="Hello World"'
        expected_output = "A valid object ID\n"

        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd(args)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_create_missing_class(self):
        "testing the create function"
        args = "create NonExistentClass"
        expected_output = "** class doesn't exist **\n"

        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd(args)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_create_update_attributes(self):
        "still testing the create function"
        args = 'create BaseModel my_attr=123 my_str="Hello_World"'
        self.console.onecmd(args)

        # Extract the created object key
        obj_key = f"BaseModel.{self.console.last_id}"

        # Get the object from storage
        created_obj = storage.all()[obj_key]

        # Check if attributes are correctly updated
        self.assertEqual(created_obj.my_attr, 123)
        self.assertEqual(created_obj.my_str, 'Hello World')

    def test_create_update_attributes_with_negative_value(self):
        "still testing the create function"
        args = "create BaseModel my_attr=-42.5"
        self.console.onecmd(args)

        obj_key = f"BaseModel.{self.console.last_id}"
        created_obj = storage.all()[obj_key]

        self.assertEqual(created_obj.my_attr, -42.5)

    def test_show(self):
        "testing the show function"
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_show_invalid_class(self):
        "test function"
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show InvalidClass 123")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")


if __name__ == '__main__':
    unittest.main()
