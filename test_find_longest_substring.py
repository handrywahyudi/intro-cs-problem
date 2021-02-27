from find_longest_substring import longest_substring
import unittest


class TestLongestSubstring(unittest.TestCase):
    def test_1(self):
        s = "abcbcd"
        self.assertEqual(longest_substring(s), "abc", "Should be 'abc'")
        print("abc")
    
    def test_2(self):
        s = "azcbobobegghakl"
        self.assertEqual(longest_substring(s), "beggh", "Should be 'beggh'")
        print("beggh")
   
    def test_3(self):
        s = "khlidfalkjduehkliudfl"
        self.assertEqual(longest_substring(s), "ehkl", "Should be 'ehkl'")
        print("ehkl")


if __name__ == "__main__":
    unittest.main()
