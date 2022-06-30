"""
Special 메소드 설명
 - 파이썬 핵심 구조 설명
 - 매직 메소드 실습
 - 클래스 매직 메소드 실습

magic method = special method

파이썬 핵심 구조 ->
    시퀀스(Sequence)
    반복(Iterator)
    함수(Functions)
    클래스(Class)

    Special Method : Class 안에 정의할 수 있는 특별한( Built-in ) 메소드
    Low Level에서 개발을 차원이 다른 개발자가 되는것.
"""

# 기본형
print(int)  # 모든 파이썬의 데이터 타입은 클래스다.
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))     # __ 로 시작하는 메소드들 확인
print(dir(float))

n = 10
print(n + 100)          # + 에서 __add__ 가 호출된다
print(n.__add__(100))       # __add__ 가 + 에 매핑된 것
# print(n.__doc__)

print(n.__bool__() , bool(n))
print(n * 100, n.__mul__(100))

print('-' * 80)

# 새로운 이름을 가진 메서드를 만들면 되는건데 기존에 내장된 메서드를 사용하는 이유가 뭐지?
# + 같은 기호로 가볍게 계산하기 위해서..?

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
print(s1 + s2)                      # + 를 할 때 내부적으로 매직메서드(__add__)가 호출됨.
print(s1 - s2)
print(s2 - s1)
print(s1 <= s2)
print(s1 >= s2)
# print(s1 < s2)
# print(s1 > s2)
print(s1)
print(s2)

# 클래스로 구현되어있어서 유지보수에 용이,
