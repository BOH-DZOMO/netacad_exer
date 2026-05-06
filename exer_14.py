class Animal():
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def speak(self):
        raise NotImplementedError

class Parrot(Animal):
    def __init__(self, name, age, language):
        super().__init__(name, age)
        self.language = language
    def speak(self):
        return f"Hello {self.language}"

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def speak(self):
        return "Meow!"

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def speak(self):
        return "Woof!"


dog1 = Dog("Rex",15)
cat1 = Cat("Whiskers", 10)
parrot1 = Parrot("Polly",6,"French")

print(dog1.speak())
print(cat1.speak())
print(parrot1.speak())

print(dog1.__dict__)
