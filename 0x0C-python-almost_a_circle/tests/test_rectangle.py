import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        rect = Rectangle(4, 6, 2, 3, 1)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    def test_getters_and_setters(self):
        rect = Rectangle(4, 6)
        rect.width = 8
        rect.height = 10
        rect.x = 5
        rect.y = 7
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 7)

    def test_area(self):
        rect = Rectangle(4, 6)
        self.assertEqual(rect.area(), 24)

    def test_display(self):
        rect = Rectangle(4, 6)
        rect.display()

        # Add assertions to verify the displayed output if needed

    def test_str_representation(self):
        rect = Rectangle(4, 6, 2, 3, 1)
        expected_str = "[Rectangle] (1) 2/3 - 4/6"
        self.assertEqual(str(rect), expected_str)



if __name__ == '__main__':
    unittest.main()
