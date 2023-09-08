class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square_rectangle(self):
        return self.width * self.height

    def perimetr_rectangle(self):
        return 2 * (self.width + self.height)


w = int(input('Введите ширину:'))
h = int(input('Введите высоту: '))
a = Rectangle(w, h)
print("Площадь а равна :", a.square_rectangle())

w = int(input('Введите ширину:'))
h = int(input('Введите высоту: '))
b = Rectangle(w, h)
print("Площадь b равна :", b.square_rectangle())

w = int(input('Введите ширину:'))
h = int(input('Введите высоту: '))
c = Rectangle(w, h)
print("Площадь с равна :", c.square_rectangle())

w = int(input('Введите ширину:'))
h = int(input('Введите высоту: '))
a = Rectangle(w, h)
print("Периметр a равн :", a.perimetr_rectangle())

w = int(input('Введите ширину:'))
h = int(input('Введите высоту: '))
b = Rectangle(w, h)
print("Периметр b равен :", b.perimetr_rectangle())

w = int(input('Введите ширину:'))
h = int(input('Введите высоту: '))
c = Rectangle(w, h)
print("Периметр с равен :", c.perimetr_rectangle())

