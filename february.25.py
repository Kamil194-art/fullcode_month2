# from abc import ABC,abstractmethod
#
# class Car(ABC):
#     def __init__(self, name, color, price):
#         self.name = name
#         self.color = color
#         self.price = price
#     def update_color(self,new_color):
#         self.color = new_color
#     def update_price(self,new_price):
#         self.price = new_price
#
#     @abstractmethod
#     def introduce(self):
#        pass
#
# bmw = Car("BMW", "black", 100_000)
# bmw.update_color("white")
# print(bmw.color)
# bmw.update_price(150_000)
# print(bmw.price)
# print(bmw.introduce())
#
#
#
# class Sportcar(Car):
#     def __init__(self,name,color,price,speed):
#         super().__init__(name,color,price)
#         self.speed = speed
#
#     def update_speed(self,new_speed):
#         self.speed += new_speed
#
#     def introduce(self):
#         return f"""
# name : {self.name}
# color : {self.color}
# price : {self.price}
# speed : {self.speed}
# """
#
#
#
# pro = Sportcar("ferrari","red",10_000_000,420)
# print(pro.speed)
# print(pro.introduce())
#
#
# class ElectricCar(Sportcar):
#     def __init__(self,name,color,price,speed,energy):
#         super().__init__(name,color,price,speed)
#         self.__energy = energy
#
#     def introduce(self):
#         return f"""
# name : {self.name}
# color : {self.color}
# price : {self.price}
# speed : {self.speed}
# energy : {self.__energy}
# time : {(self.__energy/ 500) * 8}
# """
#
# @property
# def energy(self):
#     return f"""energy : {self.__energy}
# """
#
# @energy.setter
# def energy(self,new_energy):
#     if 0 < new_energy > 100:
#         self.__energy = new_energy
#     else:
#         print("error")
#
#
# tesla1 = ElectricCar("tesla","red",120_000,200,100)
# tesla1.energy = 70
# print(tesla1.energy)

