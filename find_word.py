# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl',
# then your program should print
# Number of times bob occurs is: 2

def find_word(word, s):
    count = 0
    flag = True
    start = 0
    while flag:
        a = s.find(word, start)
        if a != -1:
            count += 1
            start = a + 1
        else:
            flag = False
    return count


if __name__ == "__main__":
    word = "bob"
    s = "azcbobobeggbobhbobakl"
    print("Number of times bob occurs is:", find_word(word, s))