class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Bird(Animal):
    def speak(self):
        return "Chirp!"

dog = Dog()
bird = Bird()

animals = [dog, bird]

for animal in animals:
    print(animal.speak())
