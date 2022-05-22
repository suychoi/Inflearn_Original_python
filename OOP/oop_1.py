# 객체지향?
# 결국은 생산성 향상!
# 재사용의 극대와, 상속, 코드의 재사용,
# 사이드 이펙트 최소화,
# 경우에 따라서는 절차지향이 더 빠른 퍼포먼스를 가질 수 있다.

# 클래스 개념
# OOP 란? 절차지향에 비해 장점,
# Self 개념
# 인스턴스 메소드
# 클래스, 인스턴스 변수

# 클래스와 인스턴스의 차이를 이해

# 네임 스페이스 : 객체를 인스턴스화 할 때 저장되는 공간, __dict__ 메서드로 확인
# 클래스 변수 : 직접 접근 가능, 공유한다.
# 인스턴스 변수 : 객체마다 별도 존재

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
# self의 이해, slef가 붙으면 인스턴스의 속성..
class SelfTest:
    def func1():        #(self) 가 없으면 클래스 메서드 이다.
        print('func1 called')
    def func2(self):
        print(id(self))     #  == print(id(f))  같다!
        print('func2 called')

f = SelfTest()        #인스턴스화
# print(dir(f)) # 사용할 수 있는 메서드 확인
print(id(f))
# f.func1()   # 에러가 난다.
# func1() takes 0 positional arguments but 1 was given  func1에서는 매개변수가 없는데 뭔가 넘어왔다.
f.func2()   #func2 called 호출 정상으로 된다.
# 즉 self 는 인스턴스를 요구한다. func2(self): 의 self에 f 가 넘어간것,

#func1 은 어떻게 호출해야 할까?
SelfTest.func1()    # 클래스로 바로 접근해서 호출한다.
SelfTest.func2(f)   # 인스턴스화된 변수 f를 매개변수로 넣어야한다.
print()
# 예제3 - 클래스 변수와 인스턴스 변수
class Warehouse:
    #클래스 변수
    stock_num = 0   #재고

    def __init__(self, name):   # 생성자
        #인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):  # 소멸자, 객체가 소멸할 때 자동으로 호출되는 함수
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)

print(user1.name)   #Lee
print(user2.name)
print(user1.__dict__)   #{'name': 'Lee'}
# class변수는 굳이 stock_num을 보여주지 않지만, user1.stock_num 으로 찾으면 클래스 속성을 알아서 찾아서 보여줍니다. ( = 인스턴스 네임스페이스에 없으면, 클래스 네임스페이스에 가서 찾는다. )
print('>>', user1.stock_num)
print(user2.__dict__)
print('before', Warehouse.__dict__)   #__dict__ = 클래스 객체의 속성 정보를 확인하기 위해 사용하는 메서드
# {'__module__': '__main__', 'stock_num': 2, '__init__': <function Warehouse.__init__ at 0x0000026112B19310>, '__del__': <function Warehouse.__del__ at 0x0000026112B193A0>, '__dict__': <attribute '__dict__' of 'Warehouse' objects>, '__weakref__': <attribute '__weakref__' of 'Warehouse' objects>, '__doc__': None}

del user1
print('after', Warehouse.__dict__)
#after {'__module__': '__main__', 'stock_num': 1, ...

# 예제4
class Dog2:
    species = 'firstdog'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def bark(self, sound):
        return "{} barks {}!".format(self.name, sound)

C = Dog2('july', 3)
D = Dog2('meme', 9)
print(C.info())
print(C.bark('Wal Wal'))
print(D.bark('Mung Mung'))
# 하나의 클래스로 여러가지 종류의 개를 만들 수 있다.

print(D.__dict__)












