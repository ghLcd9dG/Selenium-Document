import unittest

class calc(unittest.TestCase):
    def setUp(self):
        print("part of unittest start")
    def tearDown(self):
        print("part of unittest end")
    def test_add(self):
        result=1+1
        self.assertEqual(2,result)
    def test_minus(self):
        result=2-1
        self.assertEqual(1,result)
    def test_wrong_minus(self):
        result=2-1
        self.assertEqual(2,result)
def main():
    unittest.main()

if __name__ == '__main__':
    main()