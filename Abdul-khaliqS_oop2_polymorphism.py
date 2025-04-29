class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Bird(Animal):
    def speak(self):
        return "Chirp!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
bird = Bird()
cat = Cat()

animals = [dog, bird, cat]

for animal in animals:
    print(animal.speak())
