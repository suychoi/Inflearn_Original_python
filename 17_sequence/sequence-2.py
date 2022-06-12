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

# sorted : 정렬 후 새로운 객체 반환(원본 변경 안함)
# sort : 정렬 후 객체 직접 변경

f_list = ['orange', 'apple', 'strawberry', 'grape', 'peach', 'banana', 'coconut']
print()
print('original - ', f_list)
print('sorted - ', sorted(f_list))
print('original - ', f_list)
print('sorted - ', sorted(f_list, reverse=True))  # 알파벳 역순으로 정렬
print('sorted - ', sorted(f_list, key=len))     # 알파벳 길이순으로 정렬
print('sorted - ', sorted(f_list, key=lambda x: x[-1]))   # 끝에 문자를 기준으로 정렬
print('sorted - ', sorted(f_list, key=lambda x: x[-1], reverse=True))
print('original - ', f_list)

print()
print()

# sort는 반환값이 (None)
print('original - ', f_list)
print('sort - ', f_list.sort(), f_list) # 원본에 수정하는 것
print('original - ', f_list)
print('sort - ', f_list.sort(reverse=True), f_list)
print('original - ', f_list)
print('sort - ', f_list.sort(key=len), f_list)
print('original - ', f_list)
print('sort - ', f_list.sort(key=lambda x: x[-1]), f_list)
print('original - ', f_list)
print('sort - ', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)
print('original - ', f_list)

# List 와 Array의 적합한 사용방법
# 리스트 기반 : 융통성(다양한data type), 다양한 자료형, 범용적 사용
# Array 사용 : 숫자 기반, 배열(리스트와 거의 호환)













































































