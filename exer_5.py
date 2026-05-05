import random, math

num = random.randint(1, 100)
attempt = 0
try:
    while True:
        guess = int(input("Enter a guess: "))
        attempt += 1
        if guess < num:
            print("print 'Too low! Try again.")
        elif guess > num:
            print("print 'Too High! Try again.")
        elif guess==num:
            print("You are correct with ",attempt, " attempts")
            break

    print("Program terminated")

except ValueError:
    print("An error occured")