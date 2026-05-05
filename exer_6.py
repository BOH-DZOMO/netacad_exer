import math
def greet(name, greeting='Hello'):
    print(f"{greeting} {name}!")

greet("jupeter")

def sum_all(*args):
    sum = 0
    for i in args:
        if type(i) != int:
            continue
        print(i)
        sum += i
    print(sum)
sum_all('10',10,34,88)

# print(math.fsum(args))

def describe(**kwargs):
    for i, j in kwargs.items():
        print(f"{i}: {j},")

describe(name="Boh",year=3)


def profile(name, age, *hobbies, **extra):
    print(f"I am {name},{age} years old")
    print("my hobbies are ", end="") 
    print(*hobbies, sep=",")
    print("some other afacts about me are:")
    for i, j in extra.items():
        print(f"{i}: {j},")


profile("boh",130,"sleeping","singing","watching documentries",status="single")