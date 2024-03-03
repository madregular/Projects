
# hangman project 1.0
# define a function that validates whether the word is alphabetic

def word_validate(word):
    isALetter = word.isalpha()
    while not isALetter:
        print("This not word")
        word = (input("Please try again: "))
        isALetter = word.isalpha()
    else:
        print("Word Saved!")
    return word


# define a function that validates whether the guessed letter is a single letter and alphabetic
def guess_validate(guessLetter):
    isALetter = guessLetter.isalpha()
    while (not isALetter) or (len(guessLetter) > 1):
        print("This is not a letter")
        guessLetter = (input("Please try again: "))
        isALetter = guessLetter.isalpha()
    return guessLetter


def obfuscate(list1, guess1, stringDict1):
    for letter in list1:
        if letter == guess1:
            stringDict1[letter] = letter
        elif letter not in stringDict1:
            stringDict1[letter] = '_'
    print(stringDict1.values())


# request a word from the user to be guessed
masterWord = input('Hello! Please input your word. Dont let your friends see: ')

# validate the word using word_validate()
checkedWord = word_validate(masterWord)

# create a list to hold the previous guesses
prevGuess = []

stringDict = {}

# create a list holding the characters for the guessed word
wordList = set([letter for letter in masterWord])

# give a hint for how many characters are in the word
if checkedWord:
    print("There are " + str(len(masterWord)) + " characters in this word")
    underscore = (len(masterWord) * '_')
    print(underscore)

# begin the game by asking the user to guess the correct word
while len(wordList) > 0:
    # as the user to take a guess and validate
    guess = input("Take a guess!: ")
    checkedGuess = guess_validate(guess)
    obfuscate(wordList, guess, stringDict)

    # if the guess is a single digit, add it to guess list
    if len(guess) == 1:
        prevGuess.append(checkedGuess)

    # if the guessed letter is in the word, then remove it from the list
    if checkedGuess in wordList:
        print("You guessed correctly!")
        wordList.remove(checkedGuess)
    # else
    else:
        print("Sorry! Try again.")
    print(f'These are your previous guesses: {set(prevGuess)}\n')

print(f'Congratulations! You guessed the word {masterWord}!')
