class A:
    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError(f'х не может быть минус')
        self._x = value



a = A(20)
a.x = 30
print(a.x)
a.x = -1
print(a.x)
