#!/usr/bin/python3
import unittest
from ..models.base import Base


class TestBase(unittest.TestCase):
    def test_id_assigned_when_no_argument(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)
    
    def test_id_assigned_when_id_argument_provided(self):
        obj = Base(100)
        self.assertEqual(obj.id, 100)
    
    def test_id_attribute_is_public(self):
        obj = Base()
        self.assertTrue(hasattr(obj, 'id'))
    
    def test_private_attribute_is_not_accessible(self):
        obj = Base()
        with self.assertRaises(AttributeError):
            obj.__nb_objects
    
    def test_id_attribute_is_integer(self):
        obj = Base()
        self.assertIsInstance(obj.id, int)

if __name__ == '__main__':
    unittest.main()
