import random


def guess(low, high):
    random_number = random.randint(low, high)
    guess_number = 0
    while guess_number != random_number:
        guess_number = int(input(f"Guess a number between {low} and {high}: "))
        if guess_number < random_number:
            print("Sorry, guess again. Too low.")
        elif guess_number > random_number:
            print("Sorry, guess again. Too high.")
    print(
        f"🎉 Congratulation. You have guessed the number {random_number} correctly.")


low_limit = int(input("Enter the lowest range: "))
high_limit = int(input("Enter the highest range: "))
guess(low_limit, high_limit)
