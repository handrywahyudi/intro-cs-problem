from count_of_vowel_char import count_vowels
import unittest


class TestCountVowel(unittest.TestCase):
    def test_1(self):
        s = "azcbobobegghakl"
        self.assertEqual(count_vowels(s), 5, "Should be 5")
        print("Number of vowels: 5")

    def test_2(self):
        s = "abdwodrwueridfahy"
        self.assertEqual(count_vowels(s), 6, "Should be 6")
        print("Number of vowels: 6")

    def test_3(self):
        s = "idadupppdrtynb"
        self.assertEqual(count_vowels(s), 3, "Should be 3")
        print("Number of vowels: 3")


if __name__ == "__main__":
    unittest.main()