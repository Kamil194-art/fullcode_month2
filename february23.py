"""
OOP --> 2 month
"""
# class Students:
#     def __init__(self, name, age, teacher_is , nap ):
#         self.name = name
#         self.age = age
#         self.teacher_is = teacher_is
#         self.nap = nap
# student = Students("Kelsinai", 22 , "Islam" , "backend")
# print(f"""
# student
# {student.name}
# {student.age}
# {student.teacher_is}
# {student.nap}
# """)


shops = []


# class Product:
#     def __init__(self, name, price, date, sale=0):
#         self.name = name
#         self.price = price
#         self.sale = sale
#         self.date = date
#         self.acctual_price = (self.price * self.sale) / 100 if self.sale else self.price
#
#     def __str__(self):
#         return f"""
# name: {self.name}
# price: {self.price}
# sale: {self.sale}
# acctual_price: {self.acctual_price}
# date: {self.date}
# """

#     def add(self):
#         shops.append(dict(name=self.name,price=self.price,sale=self.sale,
#                           date=self.date,acctual_price=self.acctual_price))
#
# def avarenge_price(products):
#     prices = []
#     for product in products:
#         for key,value in product.items():
#             if key == 'price':
#                 prices.append(value)
#     return sum(prices)
#
#
#
#
#
# sugar = Product("sugar", 20, "12.02.2026" )
# sugar.add()
# sugar2 = Product("sugar", 20, "12.02.2026" )
# sugar2.add()
# print(shops)
# avarenge_price(shops)


# class Phone:
#     def __init__(self, name, number):
#         self.name = name
#         self.number = number
#
#     def call(self):
#         print("calling")
#
# kelsinai = Phone("Kelsinai", 43556435)
# dastan = Phone("Dastan", 43556435)

# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
#
# class Animal:
#     def __init__(self, name,say):
#         self.name = name
#         self.say = say
#
#     def speak(self):
#         engine.say(self.say)
#         engine.runAndWait()
# cat = Animal("cat","mya mya")
# dog = Animal("dog","gaf gaf")
# baran = Animal("baran","kamil sexy boy")
# baran.speak()



class Car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
audi = Car('red', 'C4', 2000)
print(f"""
color --> {audi.color}
model --> {audi.model}
year --> {audi.year} 
""")
























