# 클래스 개념, OOP와 절차지향 프로그래밍의 차이
# 클래스와 인스턴스의 차이를 이해
# 그리고 인스턴스와 객체의 차이는 ?

#클래스 변수는 : 직접 접근이 가능하고, 공유한다.
#인스턴스 변수는 : 객체마다 별도로 존재한다.

class Dog():
    sepcies = 'dog' # 클래스 변수

    def __init__(self, name, age):
        self.name = name        # 인스턴스 변수, self 가 붙음
        self.age = age

print(Dog)
a = Dog('jell', 1)
b = Dog('ceil', 3)
print('dog1', a.__dict__)
print('dog2', b.__dict__)
# print('dog3', a.__li)

print("The dog1 called {} which age {}".format(a.name, a.age))

if a.sepcies == 'dog':
    print('{} is a {}'.format(a.name, a.age))

# 클래스 변수 직접 접근하기
print(Dog.sepcies)
print(a.sepcies)

#class 선언 연습
class God:  #object 생략 가능
    #클래스 속성 self를 포함하면 인스턴스 속성이다
    def func1():
        print('func1')
    def func2(self):
        print('func2')


