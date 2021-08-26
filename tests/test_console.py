#!/usr/bin/python3
"""
    Test for the console.
"""
import unittest
import console
import os
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models.__init__ import storage


class test_console(unittest.TestCase):
    """Requirements cases
    """
    def test_to_the_module_docstring(self):
        """ Test to the module docstring.

        """
        self.assertTrue(len(console.__doc__) > 1)

    def test_to_the_class_docstring(self):
        """ Test to the class.

        """
        self.assertTrue(len(console.__doc__) > 1)

    def test_of_PEP8_console(self):
        """ Test to the pep8.

        """
        self.assertEqual(os.system("pep8 ./console.py"), 0)

    """ Console cases
    """
    def test_to_console(self):
        """ Test to the console.

        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
        self.assertIn('State'+'.'+f.getvalue()[:-1], storage.all())
