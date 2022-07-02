class Vector():
    ''' This is Class Comment '''

    def __init__(self, *args):
        ''' Created Vector Method '''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        ''' Return vector info. '''
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        '''return sum of vector value and others. '''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, other):
        return Vector(self._x * other._x, self._y * other._y)

    def __bool__(self):
        return bool(max(self._x, self._y))

v1 = Vector(2, 3)
v2 = Vector(5, 6)
v3 = Vector()

print(Vector.__init__.__doc__)
print(Vector.__doc__)
print(v1.__repr__.__doc__)
print(v1 + v2)
print(v3.__bool__())    # Max 값이 0 이니까 ~ False
print(v2.__bool__())
print(v1.__repr__())
print(v1)
print(v1 * v2)
# print(v1 * 3)      강사님 코드와 다름
print(v1 * v3)

