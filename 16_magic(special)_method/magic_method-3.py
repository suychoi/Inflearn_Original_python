'''
파이썬 데이터 모델 추상화
    - 데이터 모델 설계
    - NamedTuple 설명
    - Model Unpacking
    - NamedTuple 실습 코딩

데이터 전처리 중요, 구조적으로 만들때 튜플, 딕셔너리, 리스트, 셑, 등의 자료구조를 사용할 수 있다.
namedTuple을 사용하면 장점이 있다.
'''

# 객체 -> 파이썬의 데이터를 추상화한 것
# 모든 객체는 id, type 은 value로 확인함

# (두 점 사이의 거리 구하기 공식)
# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt   #sqrt는 루트를 씌워주는 함수

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(l_leng1)

# NamedTuple 을 활용해 만드는 경우
'''
NamedTuple 은 파이썬 클래스와는 다르고 collection module 하위의 딕셔너리와 같다.
튜플인데 딕셔너리의 성질을 갖고있는 독특한 놈이다. key 나 index로 접근이 가능하다. 
'''

from collections import namedtuple
# namedTuple 선언
Point = namedtuple('Point', 'x y')

pt3 = Point(1.0, 5.0)   # 클래스 형식으로 튜플을 추상화 함..!
pt4 = Point(2.5, 1.5)

print(pt3)              #Point(x=1.0, y=5.0)
print(pt3[0])           # index로 가져올 수 있음
print(pt3.x)            # key로 가져올 수 있음

l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)     # key로 접근하는거는 명시적으로 데이터의 흐름을 보기 좋다.
print(l_leng2)

'''
NamedTuple 선언 방법... ( 5가지 )
'''
Point1 = namedtuple('Point', ['x', 'y'])        # list 를 넣어서 선언
Point2 = namedtuple('Point', 'x,y')             # 공백없이 쉼표로 구분
Point3 = namedtuple('Point', 'x y')             # 공백으로 구분
Point4 = namedtuple('Point', 'x y x class', rename=True)             # 예약어나 중복되는 단어를 사용하는 옵션 rename=True

print()
print(Point1, Point2, Point3, Point4)           #<class '__main__.Point'> <class '__main__.Point'> <class '__main__.Point'> <class '__main__.Point'>

p1 = Point1(x=10, y=20)
p2 = Point2(20, 40)
p3 = Point3(45, y=38)
p4 = Point4(10, 20, 30, 40)                     # 개수만큼 넣어야 함.

print()
print(p1)
print(p2)
print(p3)
print(p4)       #Point(x=10, y=20, _2=30, _3=40)    파이썬이 알아서 변수를 생성해서 할당함.

'''
딕셔너리 unpacking to namedtule
'''
temp_dict = {'x':75, 'y':235}
p5 = Point1(**temp_dict)            # dictionary 지만, tuple에 언패킹이 된다.
print()
print(p5)

print(p1.x + p2.y)
x, y = p3
print(x, y)

# 네임드 튜플 메소드,
temp = [52, 38]
# _make() : 리스트를 기반으로 새로운 네임드튜플 객체 생성
p4 = Point1._make(temp)
print(p4)       #Point(x=52, y=38)

# _fields : 필드 네임 확인, key를 확인할때 굿
print(p1._fields, p2._fields, p3._fields)   #('x', 'y') ('x', 'y') ('x', 'y')

# _asdict() : Ordered Dictionary 반환 : 네임드튜플을 딕셔너리로 전환
print(p1._asdict())
print(p2._asdict())
print(p3._asdict())

### 데이터 모델링 실 사용 실습 ###
# 반 20명, 4개의 반(A,B,C,D)
Classes = namedtuple('Classes', ['rank', 'number']) # rank : A~D , number : 1 ~ 20

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

print(numbers)
print(ranks)
# List Comprehension ???
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(len(students))
print(students)

# 가독성을 위해 더 나은 방식
students2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
                    for number in [str(n)
                            for n in range(1, 21)]]

print(len(students2))
print(students2)

for s in students2:
    print(s)