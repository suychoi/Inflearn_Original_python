class Vector():

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

    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        return bool(max(self._x, self._y))



