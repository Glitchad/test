import random

numToGuess = random.randrange(1, 101)
compliment = ("kind!", "smart!", "good!", "cool!")
print(numToGuess)
guessedNum = int(
    input(
        "Welcome to Ludvig's wild and crazy guessing game!\n"
        "You have ten tries to guess a number between one and 100.\n"
        "If you fail, you'll be doomed for eternity, but if you succeed you may win a price.\n"
        "Guess a number: "
    )
)


def check_guess(num_right, tries=10):
    if guessedNum == numToGuess:
        num_right = True
        print(
            "That's right! You win! You did it in",
            10 - tries,
            "tries. Your reward is a compliment: You are",
            random.choice(compliment),
        )
        return num_right
    elif guessedNum < numToGuess:
        num_right = False
        tries -= 1
        print("That's too low,", tries, "left.")
        return num_right
    elif guessedNum > numToGuess:
        num_right = False
        tries -= 1
        print("That's too high,", tries, "left.")
        return num_right


while num_right is False and tries > 0:
    check_guess()
    guessedNum = int(input("Try again: "))

# TODO FIX SO IT STOPS DIRECTLY AFTER RIGHT ANSWER


num_right, tries = check_guess()
