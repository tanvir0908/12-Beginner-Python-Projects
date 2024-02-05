import random
from words import wordList

lives = 6

# choose a random word from that word list
chosenWord = random.choice(wordList).lower()
print("Chosen word:", chosenWord, end="\n\n")

# make empty display
display = []
for i in range(len(chosenWord)):
    display += '_'


print(display)

while lives != 0:
    # take user input
    guessedLetter = input("Guess a letter: ").lower()

    # check is that letter is in the guessed word or not
    for position in range(len(chosenWord)):
        if chosenWord[position] == guessedLetter:
            display[position] = guessedLetter
            flag = 1

    if guessedLetter not in chosenWord:
        lives -= 1
    if lives == 0:
        print("\nGame over.😣 You loose!")
        break

    if '_' not in display:
        print("\nGame over.🎉 You win!")
        break

    print("\nRemaining lives: ", lives)
    print(display)
