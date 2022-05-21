# 클래스 개념
# OOP 란? 절차지향에 비해 장점,
# 클래스, 인스턴스
# Self 개념
# 인스턴스 메소드
# 클래스, 인스턴스 변수

# 클래스와 인스턴스의 차이를 이해

#클래스 변수 : 직접 접근 가능, 공유한다.
#인스턴스 변수 : 객체마다 별도 존재

# 예제1
class Dog(object):  # 모든 class 는 object를 상속받는다.
    # 클래스 속성
    species = 'firstdog' # 클래스 변수. Dog 를 1000마리 만들어도 이건 같다.

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name    # 인스턴스 변수, 모두 다르다.
        self.age = age      # self 가 붙은거는 나만의 인스턴스 변수수
    # 인스턴스와 객체의 차이? 인스턴스가 객체에 포함된다. ?
# 클래스 정보
print(Dog)

# 인스턴스화 클래스(설계도)를 바탕으로 구현
a = Dog("mike", 2)
c = Dog("babay", 3)

# 비교
print( a == c, id(a), id(c))

# 네임 스페이스, 객체를 인스턴스화 할 때 자신만의 저장된 공간
print('dog1', a.__dict__)   #dict == dictionary
print('dog3', c.__dict__)

#인스턴스 속성 확인
print( '{} is {} and {} is {}'.format(a.name, a.age, c.name, c.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))
# 클래스 변수 직접 접근 확인
print(Dog.species)
print(a.species)
print(c.species)

# 예제2
# self의 이해, 인스턴스의 속성..
class SelfTest:
    def func1():
        print('func1 called')
    def func2(self):
        print('func2 called')
















