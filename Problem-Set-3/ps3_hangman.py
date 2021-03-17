# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    secret_word_lower_list = list(secretWord.lower())
    letters_guessed_lower = ''.join(lettersGuessed).lower()
    for letter in letters_guessed_lower:
        try:
            while True:
                secret_word_lower_list.remove(letter)
        except ValueError:
            pass

    if not secret_word_lower_list:
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    secret_word_lower_list = list(secretWord.lower())
    letter_guessed_lower_string = ''.join(lettersGuessed).lower()
    underscore_list = []
    iteration = 0
    has_letter = False
    while iteration < len(secret_word_lower_list):
        underscore_list.append("_ ")
        iteration += 1

    for letter_guessed_element in letter_guessed_lower_string:
        if letter_guessed_element in secret_word_lower_list:
            has_letter = True
            has_index_letter = [secret_word_index for secret_word_index, element in enumerate(secret_word_lower_list) if
                                element == letter_guessed_element]
            # print(has_index_letter)
            for has_letter_element in has_index_letter:
                underscore_list[int(has_letter_element)] = letter_guessed_element
                # print(underscore_list[has_index_letter])
        else:
            has_letter = False

    secret_word_string = ""
    for underscore_list_element in underscore_list:
        secret_word_string += underscore_list_element

    return secret_word_string, has_letter


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabetical_letters = string.ascii_lowercase
    alphabetical_letters_list = list(alphabetical_letters)
    for letter_guessed_element in lettersGuessed:
        letter_guessed_element = str(letter_guessed_element).lower()
        if letter_guessed_element in alphabetical_letters_list:
            alphabetical_letters_list.remove(letter_guessed_element)

    alphabetical_string = ""
    for alphabetical_letters_element in alphabetical_letters_list:
        alphabetical_string += alphabetical_letters_element

    return alphabetical_string


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game Hangman!")
    secret_word_long = len(secretWord)
    dashes = "-"
    guesses_left = 8
    letter_guessed = []
    print(secretWord)
    print("I am thinking of a word that is " + str(secret_word_long) + " letters long.")
    while guesses_left > 0:
        print(dashes * 15)
        print("You have " + str(guesses_left) + " guesses left.")
        available_letters = getAvailableLetters(letter_guessed)
        print("Available letters: " + available_letters)
        print("Please guess a letter: ")
        guess_letter = str(input()).lower()
        print(guess_letter)
        letter_guessed.append(guess_letter)
        guessed_word, has_letter = getGuessedWord(secretWord, letter_guessed)
        elem_in_letter_guessed = [index for index, element in enumerate(letter_guessed) if element == guess_letter]
        if has_letter:
            if len(elem_in_letter_guessed) < 2:
                print("Good guess:", guessed_word)
                guesses_left -= 1
            else:
                print("Oops! You've already guessed that letter:", guessed_word)

            if guessed_word == secretWord:
                break
        else:
            print("Oops! That letter is not in my word:", guessed_word)
            guesses_left -= 1

    print(dashes * 15)
    if guessed_word == secretWord:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was else.")

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)


if __name__ == '__main__':
    secretWord = chooseWord(wordlist).lower()
    secret_word = "apple"
    hangman(secret_word)

# if __name__ == '__main__':
#    letter_guessed = ['a', 'j', 'P', 'o', 'l', 'e', 'b', 'r', 't', 'q', 'm', 'j', 'n']
#    letter_guessed = ['a', 'c', 'e', 'h', 'x', 'z']
#    secret_word = 'apPLe'
#    print(isWordGuessed(secret_word, letter_guessed))
#    print(getGuessedWord(secret_word, letter_guessed))
#    print(getAvailableLetters(letter_guessed))
