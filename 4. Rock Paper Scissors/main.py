import random


def play():
    userChoice = input(
        "(R) - Rock\n(P) - Paper\n(S) - Scissors\nEnter your choice: ").upper()

    computerChoice = random.choice(['R', 'P', 'S'])

    print(
        f"Your choice is {userChoice} and Computers choice is {computerChoice}")

    if userChoice == computerChoice:
        return "🎊 The game is draw. Play again."
    if result(userChoice, computerChoice):
        return "🎉 Congratulation! You win the game."
    return "You lose. Better luck next time."


def result(user, computer):
    if (user == 'R' and computer == 'S') or (user == 'P' and computer == 'R')\
            or (user == 'S' and computer == 'P'):
        return True


limit = int(input("Enter how mane time you want to play: "))
while limit:
    print(play())
    limit -= 1
