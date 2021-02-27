# Assume s is a string of lower case characters.
#
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print
# "Longest substring in alphabetical order is: beggh"
#
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# "Longest substring in alphabetical order is: abc"


def longest_substring(s):
    start = 0
    length = 1
    maxcount = 0
    for i in range(len(s) - 1):
        if s[i + 1] < s[i]:
            length = 1
        else:
            length += 1

        if length > maxcount:
            maxcount = length
            start = i + 2 - maxcount

    result = s[start:start + maxcount]
    return result


if __name__ == "__main__":
    s = 'khlidfalkjduehkliudfl'
    print("Longest substring in alphabetical order is:", longest_substring(s))
