class Player:
    def __init__(self, name, number):
        self.name = name
        self.__number = number

    def get_number(self):
        return self.__number

    def play(self):
        print(f"{self.name} играет на поле.")

class Forward(Player):
    def play(self):
        print(f"{self.name} атакует и забивает гол!")

class Goalkeeper(Player):
    def play(self):   # полиморфизм
        print(f"{self.name} делает сейв!")

player1 = Forward("Cristiano Ronaldo", 7)
player2 = Goalkeeper("Manuel Neuer", 1)
player3 = Player("Luka Modric", 10)

team = [player1, player2, player3]

for p in team:
    p.play()
    print("Номер:", p.get_number())
    print("-" * 20)