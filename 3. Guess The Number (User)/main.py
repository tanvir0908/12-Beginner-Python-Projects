import random


def computer_guess(low, high):
    low_range = low
    high_range = high
    feedback = ""

    while feedback != 'C':
        guess = random.randint(low_range, high_range)
        print(f"The computers guess is {guess}")
        feedback = input(
            f"Is the computer guess too high (H), too low (L), or correct (C): ").upper()
        if feedback == 'H':
            high_range = guess - 1
        elif feedback == 'L':
            low_range = guess + 1
    print("🎉 Congratulation! The computer guessed the number correct.")


low_limit = int(input("Enter the lowest range: "))
high_limit = int(input("Enter the highest range: "))
computer_guess(low_limit, high_limit)
