from find_word import find_word
import unittest


class TestFindWord(unittest.TestCase):
    def test_1(self):
        word = "bob"
        s = "hdfdkbobkdruiwbobkdfowbob"
        self.assertEqual(find_word(word, s), 3, "Should be 3" )
        print("Number of times bob occurs is 3")

    def test_2(self):
        word = "tommy"
        s = "tommytoomtommytoooooommmmytommytommy"
        self.assertEqual(find_word(word, s), 4, "Should be 4" )
        print("Number of times tommy occurs is 4")

    def test_3(self):
        word = "jhon"
        s = "kielkjflajhonjhnnnnooondkfhjkd"
        self.assertEqual(find_word(word, s), 1, "Should be 1")
        print("Number of times jhon occurs is 1")


if __name__ == '__main__':
    unittest.main()
