#!/bin/python
from abc import ABC, abstractmethod
from time import sleep
import random


class Person(ABC):
    def __init__(self, age, name, money, have_home: bool):
        self.age = age
        self.name = name
        self.money = money
        self.have_home = have_home

    @abstractmethod
    def introduse_myself(self):
        raise NotImplementedError

    @abstractmethod
    def earn_money(self):
        raise NotImplementedError

    @abstractmethod
    def buy_house(self):
        raise NotImplementedError


class Human(Person):
    def __init__(self, age, name, money, have_home):
        super(Human, self).__init__(age, name, money, have_home)

    def introduse_myself(self):
        print(
            f"\nHi! I'm {self.name} and I looking for a house to purchase in my {self.age}.")
        sleep(1)

    def earn_money(self):
        while self.money < 300000:
            self.money += 20000
            print("Working hard to get more money...")
            sleep(1)
        print(f"Now I have enough money (${self.money}) to purchase a house.")
        sleep(1)

    def buy_house(self):
        if self.have_home is False and self.money >= 300000:
            self.have_home = True
            print("Now I have own house!")
            sleep(1)
        else:
            print(
                f"Maybe you already have home? ({self.have_home}) Or you don't have enough money? (${self.money})")
            sleep(1)


class House(ABC):

    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    @abstractmethod
    def apply_discount(self):
        raise NotImplementedError


class Home(House):

    def __init__(self, area, cost):
        super(Home, self).__init__(area, cost)
        self.cost = cost

    def apply_discount(self):
        print("\nHouse you interested:")
        if self.cost >= 80000 and self.area >= 40:
            self.discounted = self.cost * 0.98
            print(
                f"You can buy this one house with discounted price ${self.discounted}.")
        elif self.cost >= 200000 and self.area >= 55:
            self.discounted = self.cost * 0.96
            print(
                f"You can buy this one house with discounted price ${self.discounted}.")
        else:
            print(
                f"This house don't have discount. It's area {self.area} sq.m. and it's too small.")


class RealtorMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMetaClass):
    def __init__(self, name, min_discount):
        self.name = name
        self.discount = min_discount
        self.houses = [
            {"area": 40, "cost": 120000},
            {"area": 55, "cost": 185000},
            {"area": 62, "cost": 210000},
            {"area": 68, "cost": 285000}
        ]

    def introduse_myself(self):
        print(
            f"\nHi! I'm {self.name} and I'm selling few houses with minimum discount ${self.discount}.")
        sleep(1)

    def available_houses(self):
        print("Houses on my sell now:")
        for house in self.houses:
            print(
                f"House with area {house['area']} sq.m. is for sale now for ${house['cost']}")

    def give_discount(self):
        for house in self.houses:
            if house['area'] <= 40:
                self.discount = 3000
            else:
                self.discount = 5000

    @staticmethod
    def steal_money():
        chance = random.randint(0, 9)
        if chance == 9:
            print(f"I stole your money, you can't buy a new home now. XD")
        else:
            print(f"Oops i got caught when tried to steal your money. 8(")


if __name__ == "__main__":
    petia = Human(age=24, name="Petia", money=80000, have_home=False)
    petia.introduse_myself()
    petia.buy_house()
    petia.earn_money()
    petia.buy_house()
    home = Home(area=40, cost=100000)
    home.apply_discount()
    best_home = Home(area=60, cost=200000)
    best_home.apply_discount()
    vasia = Realtor(name="Vasia", min_discount=3000)
    vasia.introduse_myself()
    vasia.available_houses()
    vasia.give_discount()
    vasia.steal_money()
