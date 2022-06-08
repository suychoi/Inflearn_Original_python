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
print(code_list1)

# 지능형 리스트(Comprehending lists) 로 만드는 경우(더 빠른 속도)
code_list2 = [ord(s) for s in chars]
print(code_list2)

# Comprehending list + map, filter
# 자주 쓰는 방식
code_list3 = [ord(s) for s in chars if ord(s) > 40]




















