class Button:
    def __init__(self, text, link, tip):
        self.text = text
        self.link = link
        self.type = tip

    def clcik(self):
        print(f"Клик по кнопке:", self.text)


textbox = Button("textbox", '', "Кнопка")
checkbox = Button("checkbox ", '', "Кнопка")
radiobutton = Button("radiobutton ", '', "Кнопка")
webcatbles = Button("webcatbles ", '', "Кнопка")
buttons = Button("buttons", '', "Кнопка")
links = Button("links ", '', "Кнопка")
brokenlinks = Button("brokenlinks ", '', "Кнопка")
textbox.clcik()
checkbox.clcik()
radiobutton.clcik()
webcatbles.clcik()
buttons.clcik()
links.clcik()
brokenlinks.clcik()
