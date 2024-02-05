import random
from words import wordList


# choose a random word from that word list
chosenWord = random.choice(wordList).lower()
print("Chosen word:", chosenWord, end="\n\n")

# make empty display
display = []
for i in range(len(chosenWord)):
    display += '_'


print(display)

# total changes to guess
lives = 6

while lives != 0:
    # take user input
    guessedLetter = input("Guess a letter: ").lower()

    # check is that letter is in the guessed word or not
    if guessedLetter not in chosenWord:
        lives -= 1
    else:
        for position in range(len(chosenWord)):
            if chosenWord[position] == guessedLetter:
                display[position] = guessedLetter

    if lives == 0:
        print("\nGame over.😣 You loose!")
        break
    if '_' not in display:
        print("\nGame over.🎉 You win!")
        break

    print("\nRemaining lives: ", lives)
    print(display)
