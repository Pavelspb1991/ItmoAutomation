from python_trening.task_9_checks import Checks


class Input(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text


class Button(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text


class Title(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text


class Link(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text


search = Input("Лок","Текст")
Main = Title("Лок", "Текст")
wow = Link("Лок", "Текст")
knopka = Button("Лок", "Текст")


print(search.loc, search.text)
print(Main.loc, Main.text)
print(wow.loc, wow.text)
print(knopka.loc, knopka.text)

print(search.check_text())
print(Main.check_text())
print(wow.check_text())
print(knopka.check_text())

# Четыре класса и у каждого по 2 атрибута (лок и текст) +у каждого класса свой 1 обьект
