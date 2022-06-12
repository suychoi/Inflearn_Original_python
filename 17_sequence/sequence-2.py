'''
Sequence : 일렬로 나열된 순서가있는 자료구조...
파이썬 Sequence 실습
 - 튜플 고급 사용
 - Mutable(가변)
 - Immutable(불변)
 - Sort - Sorted 실습
'''

# Tuple Advanced
# Unpacing

# b, a = a, b
print(divmod(100, 9))   # 몫과 나머지 출력 함수
print(divmod(*(100, 9))) # 언패킹 풀어줘야 한다.
print(*(divmod(100,9)))

print()

# x, y, rest = range(10)  #ValueError: too many values to unpack (expected 3)
x, y, *rest = range(10)
print(x, y, rest)

x, y, *rest = range(2)    # 값이 부족한 경우엔 빈 리스트 출력
print(x, y, rest)

#Mutable vs Immutable
l = (15, 20, 25)
m = [15, 20, 25]
print(l, id(l))
print(m, id(m))
l = l * 2
m = m * 2
print(l, id(l))         # 곱해서 새로할당했기때문에 id값은 바뀐다.
print(m, id(m))
print()
l *= 2                  # 튜플은 불변형이기 때문에 새로 할당한다.
m *= 2                  # 이 때 리스트는 가변형이기 때문에, 자기 id 값을 유지한다.
print(l, id(l))
print(m, id(m))

# sort vs sorted
# reverse, key=len, key=str.lower, key=func ... key에 내가 만든 기준으로 정렬을 하겠다


















































































