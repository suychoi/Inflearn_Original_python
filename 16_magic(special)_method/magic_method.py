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









