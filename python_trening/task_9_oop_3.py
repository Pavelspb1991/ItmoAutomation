class Soda:
    def __init__(self, ing=None):
        self.ing = ing

    def show_my_drink(self):
        if self.ing:
            print(f"Газировка и {self.ing}")
        else:
            print("Обычная")


drink1 = Soda("Добавка")
drink2 = Soda()
drink1.show_my_drink()
drink2.show_my_drink()
