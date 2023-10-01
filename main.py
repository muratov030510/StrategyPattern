import random
from abc import ABC, abstractmethod


class CarNumberStrategy(ABC):
    @abstractmethod
    def number(self):
        pass


class VIPNumber1(CarNumberStrategy):
    def number(self):
        return "001, 002, 003, 004, 005, 006, 007, 008, 009, 777 and same letters"


class VIPNumber2(CarNumberStrategy):
    def number(self):
        return "001, 002, 003, 004, 005, 006, 007, 008, 009, 777 and random letters"


class MiddleNumber1(CarNumberStrategy):
    def number(self):
        return "100, 111, 200, 222, 300, 333, 400, 444, 500, 555, 600, 666, 700, 800, 888, 900, 999 and same letters"


class MiddleNumber2(CarNumberStrategy):
    def number(self):
        return "100, 111, 200, 222, 300, 333, 400, 444, 500, 555, 600, 666, 700, 800, 888, 900, 999 and random letters"


class SimpleNumber1(CarNumberStrategy):
    def number(self):
        return "010, 020, 030, 040, 050, 060, 070, 077, 080, 090, 707 and same letters"


class SimpleNumber2(CarNumberStrategy):
    def number(self):
        return "010, 020, 030, 040, 050, 060, 070, 077, 080, 090, 707 and random letters"


class RandomNumber(CarNumberStrategy):
    def number(self):
        return random.randint(1, 999)


class ChooseNumber:
    def choosen_number(self, number_gen=CarNumberStrategy):
        return number_gen.number()


if __name__ == "__main__":
    num = ChooseNumber()
    car_num = num.choosen_number(RandomNumber())
    print(car_num)