#!/bin/python

class Animal:
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def intro(self):
        print(
            f"\nThis animal has {self.color} color and is {self.age} years old.")


class Dog(Animal):
    def __init__(self, color, age, name):
        super().__init__(color, age)
        self.name = name

    def intro(self):
        print(
            f"\nThis dog called {self.name} , has {self.color} color and is {self.age} years old.")

    def bark(self):
        print("WOOF!!!")


class Cat(Animal):
    def __init__(self, color, age, name):
        super().__init__(color, age)
        self.name = name

    def intro(self):
        print(
            f"\nThis cat called {self.name} , has {self.color} color and is {self.age} years old.")

    def puke(self):
        print('''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@ <- this all is a wool from my stomach -> @@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@''')


class Bird(Animal):
    def __init__(self, color, age, wingspan):
        super().__init__(color, age)
        self.wingspan = wingspan

    def intro(self):
        print(
            f"\nThis bird has {self.color} color, it's {self.age} years old and it has {self.wingspan} m wingspan.")


class Penguin(Bird):
    def __init__(self, color, age, wingspan):
        super().__init__(color, age, wingspan)

    def intro(self):
        print(
            f"\nThis penguin has {self.color} color, it's {self.age} years old and it's {self.wingspan} wingspan is not enough to fly.")

    def fly(self):
        print("Sorry, I can't fly. I'm just a symbol of Linux. But I can swim!")

    def swim(self):
        print("Yoohoo! Let's see in deep waters!")


class Snake(Animal):
    def __init__(self, color, age, length):
        super().__init__(color, age)
        self.length = length

    def intro(self):
        print(
            f"\nThis snake has {self.color} color, it's {self.age} years old and it has {self.length} m length.")


# Use following calls to look what classes above are doing
myShurik = Dog("brown", 7, "Shurik")
myShurik.intro()
myShurik.bark()
print("Is my dog an animal?", isinstance(myShurik, Animal))

myMurzik = Cat("grey", 3, "Murzik")
myMurzik.intro()
myMurzik.puke()
print("Is my cat a bird?", isinstance(myMurzik, Bird))
print("But is it animal?", isinstance(myMurzik, Animal))

wildEagle = Bird("white", 6, 2.1)
wildEagle.intro()

wildPenguin = Penguin("black", 11, 0.75)
wildPenguin.intro()
wildPenguin.fly()
wildPenguin.swim()

python = Snake("green", 8, 7)
python.intro()
print("Is python an animal?", isinstance(python, Animal))
