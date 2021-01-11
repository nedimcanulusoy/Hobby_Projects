import random
import string


class GasStation:
    price = float(2.5)
    randGas = random.randint(0, 100)

    def __init__(self):
        self.fullTank = 100

    def getCurrentGas(self):
        print("Your current gas level is {} liters".format(self.randGas))

    def getPrice(self):
        print("Cost of per liter gas is {}$".format(self.price))

    def buyGas(self):
        self.amount = self.fullTank - self.randGas
        print("You have bought {} liter gas".format(self.amount))


class Bill(GasStation):

    def __init__(self):
        super().__init__()

    def payment(self):
        self.amount = self.fullTank - self.randGas
        letterList = [letter for letter in list(string.ascii_uppercase)]
        plateLetter = lambda: random.choices(letterList, k=3)
        plateCode = lambda: str(random.randint(100, 999))
        print("Your plate number is {}-{} and the gas cost that you need to pay is {:.2f}$".format(
            "".join(plateLetter()), plateCode(), (self.amount * self.price)))


car = GasStation()
pay = Bill()

car.getCurrentGas()
car.getPrice()
car.buyGas()
pay.payment()
