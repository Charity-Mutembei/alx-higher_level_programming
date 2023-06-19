#!/usr/bin/python3
import unittest
from models.square import Square

class SquareTest(unittest.TestCase):
    def setUp(self):
        """Create Square instances for testing"""
        self.s1 = Square(5, 2, 3, 1)
        self.s2 = Square(10, 1, 1, 2)

    def test_attributes(self):
        """Test the attributes of the Square instances"""
        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s1.x, 2)
        self.assertEqual(self.s1.y, 3)
        self.assertEqual(self.s1.id, 1)

        self.assertEqual(self.s2.size, 10)
        self.assertEqual(self.s2.x, 1)
        self.assertEqual(self.s2.y, 1)
        self.assertEqual(self.s2.id, 2)

    def test_area(self):
        """Test the area calculation of the Square instances"""
        self.assertEqual(self.s1.area(), 25)
        self.assertEqual(self.s2.area(), 100)

    def test_display(self):
        """Test the display method of the Square instances"""
        expected_output = "  ######\n  ######\n  ######\n  ######\n  ######\n"
        with unittest.mock.patch("sys.stdout", new=unittest.mock.StringIO()) as fake_stdout:
            self.s1.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_update(self):
        """Test the update method of the Square instances"""
        self.s1.update(3)
        self.assertEqual(self.s1.id, 3)

        self.s2.update(4, 7, 8, 9)
        self.assertEqual(self.s2.id, 4)
        self.assertEqual(self.s2.size, 7)
        self.assertEqual(self.s2.x, 8)
        self.assertEqual(self.s2.y, 9)

    def test_to_dictionary(self):
        """Test the to_dictionary method of the Square instances"""
        expected_dict = {
            "id": 1,
            "size": 5,
            "x": 2,
            "y": 3
        }
        self.assertEqual(self.s1.to_dictionary(), expected_dict)

        expected_dict = {
            "id": 2,
            "size": 10,
            "x": 1,
            "y": 1
        }
        self.assertEqual(self.s2.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
