import io
import unittest
import json

import items as items

from things_to_test import search_in_file, add_from_json, Storage


class TestForFunction1(unittest.TestCase):

    def setUp(self):
        lines = ['EAT\n', 'PRAY\n', 'LOVE\n']
        with open('unittest_file.txt', 'w') as self.file:
            self.file.writelines(lines)


    def test_search_in_file_positive(self):
        result = search_in_file('unittest_file.txt', 'EAT')
        self.assertEqual(result, ['EAT\n'])

    def test_search_in_file_negative(self):
        with self.assertRaises(TypeError):
            search_in_file('unittest_file.txt', 3243)

    def tearDown(self):
        self.file.close()


class TestForFunction2(unittest.TestCase):

    def setUp(self):
        data = {'a': 3, 'b': 4}
        with open('json_file_for_unittest', 'w') as self.file:
            json.dump(data, self.file)

    def test_add_from_json_positive(self):
        result = add_from_json('json_file_for_unittest', {"a": 3, "b": 4})
        self.assertEqual(result, 7)

    def test_add_from_json_negative(self):
        with self.assertRaises(TypeError):
            add_from_json('file_for_json.txt', ('a', 'b', 'c'), 15)

    def tearDown(self):
        self.file.close()

class Structure:
    item_1: list
    item_2: dict

    @classmethod
    def setUpClass(self):
        self.item_1 = []
        self.item_2 = {}

class TestStorage(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        self.storage = Storage()

    def test_add_table_positive(self):
       with self.storage.add_table('table1', self.structure):
            raise (ValueError)

    def test_add_table_negative(self):
       if self.assertIn('table1', self.storage._data):
           raise AssertionError


    def test_get_from_table_positive(self):
        with self.assertRaises(ValueError):
            return self.storage.get_from_table('table1')

    def test_get_from_table_negative(self):
        self.storage._data[1] = ['usd', 'aed']
        self.assertEqual(self.storage.get_from_table('table1'), ['usd', 'aed'])


    def test_add_to_table_positive(self):
       if self.storage.add_to_table('table4', ['currency', 'country'], {'a': 14, 'b':15}):
           raise ValueError


    def test_add_to_table_negative(self):
        with self.assertRaises(ValueError):
            return self.storage.add_to_table('table3', ['abc', 15], 185)


    def tearDown(self):
        self.storage = Storage()


















