from task_9_ import

class Input:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


class Button:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


class Title:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


class Link:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


search = Input("Лок","Текст")
Main = Title("Лок", "Текст")
wow = Link("Лок", "Текст")
knopka = Button("Лок", "Текст")

print(search.loc, search.text)
print(Main.loc, Main.text)
print(wow.loc, wow.text)
print(knopka.loc, knopka.text)

# Четыре класса и у каждого по 2 атрибута (лок и текст) +у каждого класса свой 1 обьект
