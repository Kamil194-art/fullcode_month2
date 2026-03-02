"""
hero(name,hp,damage)
archer(name,hp,damage,c)
warrior(name,hp,damage,x)
"""

# class Hero:
#     def __init__(self,name,hp,damage,):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
# class Archer:
#     def __init__(self,name,hp,damage,c):
#         super().__init__(name,hp,damage)
#         self.c = c
# class Warrior:
#     def __init__(self,name,hp,damage,x):
#         super().__init__(name,hp,damage)
#         self.x = x
# a=Warrior('Kama',200,50,2)
# b=Archer('Islam',200,50,2)
#

from reportlab.platypus import SimpleDocTemplate, Paragraph,Spacer
from reportlab.lib.styles import getSampleStyleSheet
import datetime


def create_receipt_pdf(balance, amount, operasia):
    filename = f"receipt_{operasia}.pdf"
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = [
        Paragraph("<b>BANK RECEIPT</b>", styles["Title"]),
        Spacer(1, 12),
        Paragraph(f"Operation: {operasia}", styles["Normal"]),
        Paragraph(f"Amount: {amount}", styles["Normal"]),
        Paragraph(f"Current Balance: {balance}", styles["Normal"]),
        Paragraph(f"Date: {now}", styles["Normal"]),
    ]

    doc.build(content)


class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append({
            "type": "deposit",
            "date": datetime.datetime.now(),
            "amount": amount
        })
        create_receipt_pdf(self.balance, amount, "deposit")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств")
            return

        self.balance -= amount
        self.history.append({
            "type": "withdraw",
            "date": datetime.datetime.now(),
            "amount": amount
        })
        create_receipt_pdf(self.balance, amount, "withdraw")

    def get_history(self):
        result = ""
        for record in self.history:
            result += f"{record['type']} | {record['date']} | {record['amount']}\n"
        return result

    def __str__(self):
        return f"Name: {self.name}\nBalance: {self.balance}"


user1 = Bank("Islam", 10000)
user1.deposit(100)
print(user1.get_history())
user1.withdraw(10)
print(user1.get_history())
print(user1)
