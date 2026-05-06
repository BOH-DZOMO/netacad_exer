class Factorial:
    def __init__(self):
        self._cache = {0: 1, 1: 1}

    def __call__(self, number):
        if number not in self._cache:
            self._cache[number] = number * self(number - 1)
        return self._cache[number]
    

factorial_of = Factorial()

print(factorial_of(4))
factorial_of(5)

factorial_of(6)
