#!/usr/bin/python3
import unittest
import io
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):

    def test_constructor_with_valid_arguments(self):
        """Test constructor with valid arguments"""
        r = Rectangle(5, 10, 1, 2, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 10)

    def test_constructor_with_invalid_width(self):
        """Test constructor with invalid width (negative value)"""
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 10, 1, 2)

    def test_constructor_with_invalid_height(self):
        """Test constructor with invalid height (negative value)"""
        with self.assertRaises(ValueError):
            r = Rectangle(5, -10, 1, 2)

    def test_constructor_with_invalid_x(self):
        """Test constructor with invalid x (negative value)"""
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, -1, 2)

    def test_constructor_with_invalid_y(self):
        """Test constructor with invalid y (negative value)"""
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, 1, -2)

    def test_area(self):
        """Test area calculation"""
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_update_with_args(self):
        """Test update method with positional arguments"""
        r = Rectangle(5, 10)
        r.update(20, 7, 8, 3, 4)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_update_with_kwargs(self):
        """Test update method with keyword arguments"""
        r = Rectangle(5, 10)
        r.update(id=20, width=7, height=8, x=3, y=4)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_str(self):
        """Test string representation"""
        r = Rectangle(5, 10, 1, 2, 10)
        expected_output = "[Rectangle] (10) 1/2 - 5/10"
        self.assertEqual(str(r), expected_output)


if __name__ == "__main__":
    unittest.main()
