import random


class Phone:

    brand = None
    os = None

    def __init__(self):
        self.number = "".join([str(random.randint(0, 9)) for i in (range(11))])


class IPhone(Phone):

    brand = "Apple"
    os = "iOS"


class Samsung(Phone):
    brand = "Samsung"
    os = "Android"
