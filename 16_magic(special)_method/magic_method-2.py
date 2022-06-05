"""
magic method = special method

파이썬 핵심 구조 ->
    시퀀스(Sequence)
    반복(Iterator)
    함수(Functions)
    클래스(Class)

    Special Method : Class 안에 정의할 수 있는 특별한(built in) 메소드
    Law Level에서 개발을 하는거는 차원이 다른 개발자가 되는것.
"""

# 클래스 예제2
# 벡터 계산하는 경우,
# (5,2) + (4,3) = (9,5)
# (10,3) * 5 = (50, 15)
# (5, 10) = 10 Max 함수, 이런 기능을 미리 정의해서 만들어놓는 실습

class Vector():
    def __init__(self, *args):           # 패킹으로 받기
        '''        Create a vector, example : v = Vector(5, 10)        '''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        '''        Return vector informations.        '''
        return 'Vector(%r, %r)' % (self._x, self._y)        # raw data 입력받기

    def __add__(self, other):
        ''' Return sum of vector value and others.'''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        return bool(max(self._x, self._y))  # (0, 0) 인지 확인하는 메소드~



print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)

# Vector 인스턴스 생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()       # 값이 없으면 0,0 으로 되도록 해놓음!

# 매직 메소드 출력,
print()
print(v1, v2, v3)
print(v1 + v2)
print(v2 + v3)
print()
print(v1 * 2)
print(v2 * 3)
print(v3 * 3)
print()
print(bool(v1))
print(bool(v2))
print(bool(v3))
print()

if bool(v3):    #False
    print('confirm')

# 두 점 사이 거리 구하기?
