from library_book import book
import unittest

class book_test(unittest.TestCase):
    global instance
    instance=book(name="Harry Potter",page=350)

    def test_init(self):
        self.assertEqual(instance.name,"Harry Potter")
        self.assertEqual(instance.page,350)
        self.assertTrue(isinstance(instance, dict))

    def test_key(self):
        instance.key1='value1'
        self.assertTrue('key1' in instance)
        self.assertEqual(instance.key1, 'value1')

    def test_attr_add(self):
        instance["key2"]="value2"
        self.assertTrue('key2' in instance)
        self.assertEqual(instance.key2, 'value2')

    def test_keyerror(self):
        with self.assertRaises(KeyError):
            instance['empty']

    def test_attrerror(self):
        with self.assertRaises(AttributeError):
            instance.empty
def main():
    unittest.main()

if __name__ == '__main__':
    main()