""" don't repeat yourself (DRY) """
class Kamil:
    def __init__(self, name,age,height):
      self.name = name
      self.age = age
      self.height = height
kamil = Kamil("Kamil",14,168)
print(f"""
Name: {kamil.name}
Age: {kamil.age}
Height: {kamil.height}
""")

class Altysh(Kamil):
    def __init__(self,name,age,height):
        super().__init__(name,age,height)
altynai = Altysh("Altynai",18,165)
print(f"""
Name: {altynai.name}
Age: {altynai.age}
Height: {altynai.height}
""")

class Alinur(Kamil):
    def __init__(self,name,age,height):
        super().__init__(name,age,height)
alinur = Alinur("Alinur",12,155)
print(f"""
Name: {alinur.name}
Age: {alinur.age}
Height: {alinur.height}
""")






























