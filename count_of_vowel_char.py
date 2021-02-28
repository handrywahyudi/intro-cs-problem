# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

def count_vowels(s):
    char_list = list(s)
    vowel_list = ['a', 'i', 'u', 'e', 'o']
    result_list = []
    for i in char_list:
        if i in vowel_list:
            result_list.append(i)

    return len(result_list)


if __name__ == '__main__':
    s = "azcbobobegghakl"
    print("Number of vowels:", count_vowels(s))
