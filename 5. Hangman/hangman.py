import random
# from words import word_list

wordList = ["Apple", "Potato", "Orange"]
lives = 6

# choose a random word from that word list
chosenWord = random.choice(wordList).lower()

# make empty display
display = []
for i in range(len(chosenWord)):
    display += '_'

print(chosenWord)
print(display)

while lives > 0:
    # take user input
    guessedLetter = input("Guess a letter: ").lower()

    # check is that letter is in the guessed word or not
    for position in range(len(chosenWord)):
        if chosenWord[position] == guessedLetter:
            display[position] = guessedLetter
            flag = 1

    if guessedLetter not in chosenWord:
        lives -= 1
    print("Lives: ", lives)
    print(display)
