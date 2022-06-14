
class Device:
    
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    
    def printBrand(self):
        print('Phone brand:',self.brand)

class Phone(Device):
    
    def __init__(self,brand,price,number):
        self.brand = brand
        self.price = price
        self.number = number
    
    def printNumber(self):
        print('The phone number is:',self.number)


phone = Phone('LG',3500,6621456789)
phone.printNumber()
phone.printBrand()