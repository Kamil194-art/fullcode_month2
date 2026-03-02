""" Инкапсуляция """
class Shop:
    def __init__(self,name,term,price,):
        self.__name = name
        self.__term = term
        self.__price = price
    def getter(self):
        return self.__price
    def setter(self,price):
        if price > 0:
            self.__price = price
asia = Shop("milk",25,80)
print(asia.getter())
asia.setter(90)
print(asia.getter())