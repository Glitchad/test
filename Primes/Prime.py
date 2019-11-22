x = int(
    input("This program checks whether an integer is a prime. Please enter a number: ")
)

if x > 1:
    for item in range(2, x + 1):
        if (x % item) == 0:
            print(x, "is not a prime.")
            print(item, "times", x // item, "is", x)
            break
        else:
            print(x, "is a prime!")
            continue
    else:
        print(x, "is not a prime.")
else:
    print(x, "is not a prime.")
