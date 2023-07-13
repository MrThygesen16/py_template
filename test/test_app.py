from my_project import app
import unittest

class appTest(unittest.TestCase):

    def test_plus_one(self):
        assert app.plus_one(1) == 2
    
    def test_plus_one_fail(self):
        assert app.plus_one(1) == -1


if __name__ == "__main__":
    unittest.main() # run all tests
    
    # test change