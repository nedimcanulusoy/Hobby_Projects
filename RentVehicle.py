import datetime


class RentVehicle:

    def __init__(self, stock=0, dailyPrice=65, monthlyPrice=50):
        self.stock = stock
        self.dailyPrice = dailyPrice
        self.monthlyPrice = monthlyPrice

    def getStock(self):
        return "{} vehicles available to rent.".format(self.stock)

    def stockUpdate(self, add):
        self.stock += add
        return "{} vehicles have added to stock.".format(self.stock)

    def rentDaily(self, RequestedCarNumber):

        if RequestedCarNumber <= 0:
            return "We do not have vehicle right now, sorry!"

        elif RequestedCarNumber > self.stock:
            return "Sorry! We have currently {} vehicle(s) available to rent.".format(self.stock)

        else:
            self.stock -= RequestedCarNumber
            currentTime = datetime.datetime.now()
            return "You have rented a {} vehicle(s) on daily basis today at {}.".format(RequestedCarNumber,
                                                                                        currentTime.day,
                                                                                        currentTime.month,
                                                                                        currentTime.year)
            # .format(RequestedCarNumber, currentTime.strftime("%A %d %B %Y"))

    def rentMonthly(self, RequestedCarNumber):

        if RequestedCarNumber <= 0:
            return "We do not have vehicle right now, sorry!"

        elif RequestedCarNumber > self.stock:
            return "Sorry! We have currently {} vehicle(s) available to rent.".format(self.stock)

        else:
            self.stock -= RequestedCarNumber
            currentTime = datetime.datetime.now()
            return "You have rented a {} vehicle(s) on monthly basis today at {}.{}.{}.".format(RequestedCarNumber,
                                                                                                currentTime.day,
                                                                                                currentTime.month,
                                                                                                currentTime.year)

    def returnVehicle(self, rentalBasis, rentalTime, numOfVehicles):

        bill = 0

        if rentalTime and rentalBasis and numOfVehicles:
            self.stock += numOfVehicles
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            if rentalBasis == 1:
                if numOfVehicles >= 10:
                    bill = ((rentalPeriod.seconds / 3600 * 24) * numOfVehicles * (
                            self.dailyPrice - (self.dailyPrice / 5)))
                    return "Thanks for returning your vehicle. Hope you enjoyed our service!\nThat would be ${}".format(
                        bill)
                else:
                    bill = ((rentalPeriod.seconds / 3600 * 24) * numOfVehicles * (self.dailyPrice))
                    return "Thanks for returning your vehicle. Hope you enjoyed our service!\nThat would be ${}".format(
                        bill)


            elif rentalBasis == 2:
                if numOfVehicles >= 10:
                    bill = ((rentalPeriod.seconds / 3600 * 24 * 24) * numOfVehicles * (
                            self.monthlyPrice - (self.monthlyPrice / 10)))
                    return "Thanks for returning your vehicle. Hope you enjoyed our service!\nThat would be ${}".format(
                        bill)
                else:
                    bill = ((rentalPeriod.seconds / 3600 * 24 * 24) * numOfVehicles * (self.monthlyPrice))
                    return "Thanks for returning your vehicle. Hope you enjoyed our service!\nThat would be ${}".format(
                        bill)
