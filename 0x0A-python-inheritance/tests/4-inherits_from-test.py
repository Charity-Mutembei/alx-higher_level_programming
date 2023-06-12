import unittest
import importlib.util

spec = importlib.util.spec_from_file_location('inherits_from_module', '4-inherits_from.py')
inherits_from_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(inherits_from_module)
inherits_from = inherits_from_module.inherits_from

# def inherits_from(obj, a_class):
#     return issubclass(type(obj), a_class) and type(obj) is not a_class


class TestInheritsFrom(unittest.TestCase):

    def test_inherits_from_direct(self):
        class MyBaseClass:
            pass

        class MySubClass(MyBaseClass):
            pass

        obj = MySubClass()
        self.assertTrue(inherits_from(obj, MyBaseClass))

    def test_inherits_from_indirect(self):
        class MyBaseClass:
            pass

        class MySubClass(MyBaseClass):
            pass

        class MyChildClass(MySubClass):
            pass

        obj = MyChildClass()
        self.assertTrue(inherits_from(obj, MyBaseClass))

    def test_not_inherits_from_same_class(self):
        class MyBaseClass:
            pass

        obj = MyBaseClass()
        self.assertFalse(inherits_from(obj, MyBaseClass))

    def test_not_inherits_from_unrelated_class(self):
        class MyBaseClass:
            pass

        obj = int(10)
        self.assertFalse(inherits_from(obj, MyBaseClass))


if __name__ == '__main__':
    unittest.main()
