""" Абстракция """
from abc import ABC, abstractmethod
class Animal(ABC):
    def init(self, name):
        self.name = name
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print(f"{self.name} говорит: Гав-гав")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} говорит: Мяу")

class Cow(Animal):
    def speak(self):
        print(f"{self.name} говорит: Му-у")
dog = Dog("Шарик")
cat = Cat("Мурка")
cow = Cow("Бурёнка")
animals = [dog, cat, cow]
for animal in animals:
    animal.speak()
