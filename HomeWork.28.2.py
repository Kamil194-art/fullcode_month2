class Airplane:
    def __init__(self, model, capacity):
        self.model = model
        self.__capacity = capacity

    def get_capacity(self):
        return self.__capacity

    def fly(self):
        print(f"Самолет {self.model} летит.")

class PassengerPlane(Airplane):
    def fly(self):
        print(f"Пассажирский самолет {self.model} перевозит пассажиров.")

class CargoPlane(Airplane):
    def fly(self):
       print(f"Грузовой самолет {self.model} перевозит груз.")

class Airport:
    def __init__(self, name):
        self.name = name
        self.planes = []

    def add_plane(self, plane):
        self.planes.append(plane)

    def start_flights(self):
        print(f"Аэропорт {self.name} начинает рейсы:\n")
        for plane in self.planes:
            plane.fly()
            print("Вместимость:", plane.get_capacity())
            print("-" * 25)

plane1 = PassengerPlane("Boeing 737", 180)
plane2 = CargoPlane("Airbus A330", 70)

airport = Airport("Manas International")

airport.add_plane(plane1)
airport.add_plane(plane2)

airport.start_flights()