'''
03_data_type : tuple 참고

튜플은 리스트와 비교해서 기억한다.
튜플 자료형은 순서가 있고,
중복이 가능하다.
하지만 수정과 삭제가 안되는 특징이 있다.

'''

a = (1)             # 튜플 선언
t2 = 1, 2, 3        # 튜플 선언
b = (1, ) # 하나의 요소만 선언할대는  콤마를 붙여야 한다.
print(type(a), type(b))
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captain')
e = (100, 1000, ('Ace', 'Base', 'Captain'))

print(d[0] + d[1])  # 1100
print(e[-1][1])     #Base

# 튜플 연산에서 길이가 늘어나는 것은 허용한다.
print(c + d)
print(c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print(a.index(3))
print(a.count(2))

# 패킹과 언패킹 ( packing, unpacking )
# 패킹은 묶는다.
t = ('foo', 'bar', 'baz', 'qux')
# 언패킹1 ( 패킹된 튜플에서 요소를 할당해준다. )
(x1, x2, x3, x4) = t
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 패킹 언패킹 실습
t2 = 1, 2, 3
print(type(t2))
t3 = 4,         # 괄호 생략해도 튜플이 된다.
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6
print(t2)
print(t3)

print(x1, x2, x3)
print(x4, x5, x6)