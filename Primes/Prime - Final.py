# define input variable
inputNum = int(
    input("This program checks whether an integer is a prime. Please enter a number: ")
)
isPrime = None

if inputNum > 2:
    for item in range(2, inputNum):
        if (inputNum % item) == 0:
            print(item, "*", inputNum // item, "=", inputNum)
            isPrime = False
            break
        else:
            isPrime = True
elif inputNum == 2:
    isPrime = True

if isPrime:
    print(inputNum, "is a prime!")
else:
    print(inputNum, "is not a prime!")
