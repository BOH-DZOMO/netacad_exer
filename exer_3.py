for i in range(1, 51):
    x= i%3
    y= i%5 
    if (x==0) and (y==0):
        print("FizzBuzz", end=" ")
    elif x==0:
        print("Fizz", end=" ")
    elif y==0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")