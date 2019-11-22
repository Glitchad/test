x = int(
    input("This program checks whether an integer is a prime. Please enter a number: ")
)

isPrime = None

if x > 1:
    for item in range(2, x + 1):
        if (x % item) == 0:
            isPrime = False
        else:
            isPrime = True
    else:
        isPrime = False
else:
    isPrime = False

if isPrime:
    print(x, "is a prime!")
else:
    print(x, "is not a prime")
    print(item, "times", x // item, "is", x)
