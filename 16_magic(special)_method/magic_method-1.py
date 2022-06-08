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

# 기본형
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10
print(n + 100)          # + 에서 __add__ 가 호출된다
print(n.__add__(100))
# print(n.__doc__)

print(n.__bool__() , bool(n))
print(n * 100, n.__mul__(100))

print()

# 예제1
class Fruit():
    def __init__(self, _name, _price):
        self._name = _name
        self._price = _price

    def __str__(self):
        return 'Fruit Class Info : {} {}'.format(self._name, self._price)

    def __add__(self, x):
        print('__add__')
        return self._price + x._price

    def __sub__(self, x):
        print('__sub__')
        return self._price - x._price

    def __le__(self, x):
        print('__le__')
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self, x):
        print('__ge__')
        if self._price >= x._price:
            return True
        else:
            return False

# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Mango', 2500)

# 일반적인 경우 계산은 이렇게 하지만
print(s1._price + s2._price)
# 매직 메소드를 만들어 놓은 경우
print(s1 + s2)
print(s1 - s2)
print(s2 - s1)
print(s1 <= s2)
print(s1 >= s2)
# print(s1 < s2)
# print(s1 > s2)
print(s1)
print(s2)

# 클래스로 구현되어있어서 유지보수에 용이,