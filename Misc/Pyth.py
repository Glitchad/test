num1 = 1

while True:
    num1 = num1 + 1

    for i in range(2, num1):
        if (num1 % i) == 0:
            print("Not prime")
        else:
            print(num1)

print("Done!")
