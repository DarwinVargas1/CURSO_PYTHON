"""Java — necesitas el tipo exacto
Dog dog = new Dog();
dog.speak(); // solo funciona con Dog"""

# Duck Typing — solo necesitas el método correcto, o sea que el objeta tenga el método
"""
class Dog:
    def speak(self):
        print("Woof!")

dog=Dog()
dog.speak() # Woof!"""