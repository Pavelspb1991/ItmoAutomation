class Car:
    def __init__(self, color, type_1, year):
        self.color = color
        self.type_1 = type_1
        self.year = year

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль заглушен")

    def year(self, year_new):
        self.year = year_new

    def type_1(self):
        self.type_1 = "hatchback"

    def color(self):
        self.color = "silver"


