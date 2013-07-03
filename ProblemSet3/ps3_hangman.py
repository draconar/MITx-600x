# 6.00 Problem Set 3
# 
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
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    it = 0
    for char in secretWord:
        if char in lettersGuessed: it += 1
    if len(secretWord) == it: return True
    else: return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    it = 0
    sw = list(secretWord)
    for element in sw:
        if element not in lettersGuessed: sw[it] = '_ '
        it += 1
    return "".join(sw)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letters = list('abcdefghijklmnopqrstuvwxyz')
    for char in lettersGuessed:
        if char in letters: letters.remove(char)
    return "".join(letters)
    
    

def hangman(secretWord):
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(secretWord), 'letters long.'
    guesses = 8
    lettersGuessed = []
    lettersall = list('abcdefghijklmnopqrstuvwxyz')
    quess = 0
    while (isWordGuessed(secretWord, lettersGuessed) == False) and (guesses > 0):
        print '-------------'
        print 'You have', guesses, 'guesses left.'
        print 'Available letters: ', getAvailableLetters(lettersGuessed)
        guessletter = raw_input('Please guess a letter: ')
        guess = guessletter.lower()
        if guess in lettersGuessed: print 'Oops! You\'ve already guessed that letter:', getGuessedWord(secretWord, lettersGuessed)
        elif guess in secretWord:
            lettersGuessed += guess
            print 'Good guess:', getGuessedWord(secretWord, lettersGuessed)
        elif guess not in secretWord:
            guesses -= 1
            lettersGuessed += guess
            print 'Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed)
    if (isWordGuessed(secretWord, lettersGuessed) == True):
        print '-------------'
        print 'Congratulations, you won!'
    else:
        print '-----------'
        print 'Sorry, you ran out of guesses. The word was', secretWord


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
