def check_guess(tries, num_right):
    tries = 10
    if numToGuess > guessedNum:
        num_right = False
        print("Number too low.")
        return num_right
    elif numToGuess < guessedNum:
        num_right = False
        print("Number too high.")
        return num_right
    elif numToGuess == guessedNum:
        num_right = True
        return num_right


while check_guess(num_right=False):
