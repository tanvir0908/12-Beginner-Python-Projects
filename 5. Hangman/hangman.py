import random
# from words import word_list

wordList = ["Apple", "Potato", "Orange"]

# choose a random word from that word list
chosenWord = random.choice(wordList)

display = []
for i in range(len(chosenWord)):
    display += '_'

print(chosenWord)
print(display)

# take user input
guessedLetter = input("Guess a letter: ")

# check is that letter is in the guessed word or not
for letter in chosenWord:
    if letter == guessedLetter:
        print("Matched")
    else:
        print("No match")
