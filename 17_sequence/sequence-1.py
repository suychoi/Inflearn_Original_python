'''
Sequence : 일렬로 나열된 순서가있는 자료구조...
파이썬 자료형 ( 은 크게 두 가지로 나뉜다. )
    1. 컨테이너(Container : 서로 다른 자료형을 담을 수 있는[list, tuple, collections.deque)
        [3, 3.0, 'a] 같은 다른 자료형 가능
    2. 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])

    가변형(list, bytearray, array.array, memoryview, deque)
    불변형(tuple, str, bytes)

'''

# 리스트 및 튜플 고급
# 유니코드 리스트로 만드는 경우
chars = '!@#$%^&*()_+'
code_list1 = []

for s in chars:
    code_list1.append(ord(s))

# 지능형 리스트(Comprehending lists) 로 만드는 경우(더 빠른 속도)
code_list2 = [ord(s) for s in chars]

# Comprehending list + map, filter
# 자주 쓰는 방식
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))   # filter 필터 적용

# 전체 출력
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)

# chr 로 문자로 복구 확인
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

# Generator 생성 sequence result를 반환, 메모리 사용량을 적게 for 문을 돌릴수있다.
import array
# array = 플랫, 가변형(위에서 확인)
print(dir(chars))   # __iter__ 의 존재 확인, 이게 있으면 연속적인 값으로 for문으로 돌릴수있다는 뜻

tuple_g = (ord(s) for s in chars)
print(tuple_g)      #<generator object <genexpr> at 0x000001728D730740>
print(type(tuple_g))
print(next(tuple_g)) # next로 다음 값을 반환하는데,
print(next(tuple_g))

array_g = array.array('I', (ord(s) for s in chars))
print(array_g)
print(type(array_g))
print(array_g.tolist())     # Array 를 list로 변환
print()

# 제네레이터 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21)))
for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21)):
    print(s)
    # 하나 생성하고 하나 출력하고 해서 메모리를 아낌

# list 깊은복사와 얕은 복사의 차이!!
# 리스트 주의 사항
marks1 = [['~'] * 3 for _ in range(4)]  # 반복은 하지만 사용은 안하는 경우 _ 로 사용도 가능
print(marks1)

marks2 = [['~'] * 3] * 4
print(marks2)

# marks1 과 marks2 는 똑같이 생겼지만, 다음에서 차이가 난다.
marks1[0][1] = 'X'
marks2[0][1] = 'X'

print()
print(marks1)
print(marks2)
# [['~', 'X', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
# [['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~']]
# 1번은 id 값이 다른 것, 2번은 id값도 같이 복제가 되어 이렇게 되는것. ...

# 증명
print([id(i) for i in marks1])
print([id(i) for i in marks2])  # 2번은 다 같은 id를 공유
















