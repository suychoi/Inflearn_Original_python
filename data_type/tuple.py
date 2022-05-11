# 튜플은 리스트와 비교하는게 중요하다.
# 튜플 자료형(순서o, 중복o, 수정 X, 삭제X) 불변

#튜플 선언
a = (1)
b = (1,)
print(type(a), type(b))
#<class 'int'> <class 'tuple'> 하나만 선언할 때는 뒤에 콤마를 붙여야 한다.
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captain')
e = (100, 1000, ('Ace', 'Base', 'Captain'))

print("인덱싱")
print(d[1])
print(d[0] + d[1])
print(e[-1][1])
print(list(e[-1][1]))

#슬라이싱
print(d[0:3])
print(d[2:])
print(e[-1][1:3])

#튜플 연산 길이가 늘어나는 것은 허용한다.
print(c + d)
print(c * 3)

#튜플 함수
a = (5, 2, 3, 1, 4)
print(a)
print(a.index(3))
print(a.count(2))

#튜플에서의 팩킹과 언팩킹(Packing, Unpacking)
#팩킹(묶는다.)
t = ('foo', 'bar', 'baz', 'qux')
#언팩킹1 ( 패킹된 튜플에서 요소를 할당해줌)
(x1, x2, x3, x4) = t
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

#팩킹 언팩킹 실습
t2 = 1, 2, 3
t3 = 4, #괄호는 생략
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)