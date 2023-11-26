#!usr/bin/python3
""" Unit test for HBNBCommand class. """
import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
import json
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """ Test the HBNBCommand class. """

    def test_emptyline(self):
        """ Test empty line + ENTER shouldn't execute. """
        with patch("sys.stdout", new_callable=StringIO):
            self.cmd.onecmd("\n")
            output = sys.stdout.getvalue()
            self.assertEqual(output, "")

    def test_eof(self):
        """ Test the 'EOF' command. """
        with self.assertRaises(SystemExit):
            self.cmd.onecmd("EOF")

    def test_help(self):
        """ Test the 'help' command. """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("help")
            output = mock_stdout.getvalue()
            self.assertIn("Documented commands (type help <topic>):", output)

    def test_create_missing_class(self):
        """ Test the 'create' command with missing class name. """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("create")
            output = mock_stdout.getvalue()
            self.assertEqual(output, "** class name missing **\n")

    def test_create_invalid_class(self):
        """ Test the 'create' command with invalid class name. """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("create InvalidClass")
            output = mock_stdout.getvalue()
            self.assertEqual(output, "** class doesn't exist **\n")

    def test_show(self):
        """ Test the 'show' command. """
        obj = BaseModel()
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd(f"show BaseModel {obj.id}")
            output = mock_stdout.getvalue()
            self.assertIn(str(obj), output)

    def test_show_missing_class(self):
        """ Test the 'show' command with missing class name. """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("show")
            output = mock_stdout.getvalue()
            self.assertEqual(output, "** class name missing **\n")

    def test_show_invalid_class(self):
        """ Test the 'show' command with invalid class name. """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("show InvalidClass")
            output = mock_stdout.getvalue()
            self.assertEqual(output, "** class doesn't exist **\n")

    def test_show_missing_id(self):
        """ Test the 'show' command with missing instance id. """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("show BaseModel")
            output = mock_stdout.getvalue()
            self.assertEqual(output, "** instance id missing **\n")

    def test_destroy(self):
        """ Test the 'destroy' command. """
        obj = BaseModel()
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd(f"destroy BaseModel {obj.id}")
            output = mock_stdout.getvalue()
            self.assertEqual(output, "")

    def test_destroy_invalid_class(self):
        """ Test the 'destroy' command with invalid class name. """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("destroy InvalidClass")
            output = mock_stdout.getvalue()
            self.assertEqual(output, "** class doesn't exist **\n")

    def test_destroy_missing_id(self):
        """ Test the 'destroy' command with missing instance id. """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("destroy BaseModel")
            output = mock_stdout.getvalue()
            self.assertEqual(output, "** instance id missing **\n")

    def test_destroy_invalid_id(self):
        """ Test the 'destroy' command with invalid instance id. """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("destroy BaseModel invalid_id")
            output = mock_stdout.getvalue()
            self.assertEqual(output, "** no instance found **\n")

    def test_all(self):
        """ Test the 'all' command. """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("all")
            output = mock_stdout.getvalue()
            self.assertIn("BaseModel", output)

    def test_all_missing_class(self):
        """ Test the 'all' command with missing class name. """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("all InvalidClass")
            output = mock_stdout.getvalue()
            self.assertEqual(output, "** class doesn't exist **\n")

    def test_update(self):
        """ Test the 'update' command. """
        obj = BaseModel()
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd(f'update BaseModel {obj.id} name "new_name"')
            output = mock_stdout.getvalue()
            self.assertEqual(output, "")

    def test_update_invalid_class(self):
        """ Test the 'update' command with invalid class name. """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd('update InvalidClass')
            output = mock_stdout.getvalue()
            self.assertEqual(output, "** class doesn't exist **\n")

    def test_update_missing_id(self):
        """ Test the 'update' command with missing instance id. """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd('update BaseModel')
            output = mock_stdout.getvalue()
            self.assertEqual(output, "** instance id missing **\n")

    def test_update_missing_value(self):
        """ Test the 'update' command with missing attribute value. """
        obj = BaseModel()
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd(f'update BaseModel {obj.id} name')
            output = mock_stdout.getvalue()
            self.assertEqual(output, "** value missing **\n")

    def test_update_no_attribute(self):
        """ Test the 'update' command with a non-existent attribute. """
        obj = BaseModel()
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd(
                f'update BaseModel {obj.id} non_existent_attr "new_value"'
            )
            output = mock_stdout.getvalue()
            self.assertEqual(output, "")


if __name__ == '__main__':
    unittest.main()
