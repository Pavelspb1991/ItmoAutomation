class A:
    def __init__(self):
        self.x = 10


class B(A):
    def __init__(self):
        super().__init__()
        self.y = self.x + 5


b = B()
print(B().y)

print(b.y)
