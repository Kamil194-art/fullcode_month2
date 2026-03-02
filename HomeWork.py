""" Наследование """
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
kamil = Student("Kamil", 14)
print(f"""
Name: {kamil.name}
Age: {kamil.age}
""")
class Boy(Student):
    def __init__(self, name, age,born):
        super().__init__(name, age)
        self.born = born
islam = Boy("Islam",23,2003 )
print(f"""
Name: {islam.name}
Age: {islam.age}
Born: {islam.born}
""")
class Girl(Boy):
    def __init__(self, name, age,born,iq):
        super().__init__(name,age,born)
        self.iq = iq
kelsinai = Girl("Kelsinai",22,2004,110 )
print(f"""
Name: {kelsinai.name}
Age: {kelsinai.age}
Born: {kelsinai.born}
Iq: {kelsinai.iq}
""")


































































