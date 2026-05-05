try:
    num1 = int(input("Enter the first num: "))
    num2 = int(input("Enter the second num: "))
    print(num1+num2, num1-num2, num1*num2, num1/num2, num1//num2, num1%num2, num1**num2)

    if num1%num2 == 0:
        print(f"{num1} is divisible by {num2}")
    else:
        print(f"{num1} is not divisible by {num2}")
    print(num1/num2,int(num1/num2))
    print((num1+num2)/2)
except:
    print("an error occurred, try again")