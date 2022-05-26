# 파이썬 내장함수
# 자주 사용하는 함수 위주로 실습
# 사용하다보면 자연스럽게 숙달

# 절대값
# abs()
print(abs(-3))

x = 'qwe'
# all, any : iterable(반복가능한 list, tuple, set ... ) 요소 검사(참, 거짓)
print(all([1,2,3,0]))    # and 조건   0 이나 '' 같은 빈 요소에 대해서 검사 즉 모든 값이 True 여야 한다.
print(any([1,2,0]))      # or 조건

# chr : 아스키 -> 문자
# ord : 문자 -> 아스키

print(chr(67))

# enumerate : 인덱스 + Iterable 객체 생성
for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i +1 , name)

# filter : 반복가능한 객체 요소를 지정한 함수 조건(True)에 맞는 값만 추출
def conv_pos(x):
    return abs(x) > 2
# 함수를 호출하지 않고 명시만 해도 filter 에서 호출해준다.
print(filter(conv_pos, [1, -3, 2, 0, -5, 6]))   #<filter object at 0x00000216D94D2F40>
print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6]))) #[-3, -5, 6]

# 람다함수로 활용하기.
print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 0, -5, 6])))

# id : 객체의 주소값(래퍼런스) 반환
print(id(int(5)))

# len 요소의 길이 반환
print(len('asdfzxcvr'))

# max, min 최대, 최소값
print(max([1,2,5,6]))
print(max('pytthon study z'))
print(min([1,2,5,6]))

# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)
print(list(map(conv_abs, [1, 2, -1, -3, -5, -6, -7, -23])))
print(list(map(lambda x: abs(x), [1, 2, -1, -3, -5, -6, -7, -23])))
# map은 함수를 통과시켜서 나오는 값..!

# pow 함수 : 제곱값 반환
print(pow(2,10))    #1024

# range 함수 반복 가능한 객체(Iterable) 반환
print(list((range(1, 9, 2))))

# round : 반올림 함수
print(round(6.5139, 2)) # 둘째자리에서 반올림
print(round(5.6))   # 첫재짜리에서 반올림 됨

# sorted : 반복 가능한 객체(Iterable)를 정렬 후 반환,
print(sorted([6, 7, 4, 2, 46, 83]))     # 오름차순

print(sorted(['p', 'y', 't', 'h', 'o', 'n']))

# sum : 반복 가능한 객체(Iterable)의 합을 반환
print(sum((6, 7, 8, 9, 10)))

# type : 자료형 반환
print(type('sel'))
print(type({}))
print(type(()))

# zip : 반복 가능한(Iterable) 객체의 요소를 묶어서 반환
print(list(zip([10,20,30],[40,50,60],[70,80,90])))
#[(10, 40, 70), (20, 50, 80), (30, 60, 90)]
print(list(zip([10,20,30],[40,50,60],[70,80])))
#[(10, 40, 70), (20, 50, 80)]       짝이 없는 경우는 묶이지 않는다.

# inemulate, filter, map 은 꼭 알아야 합니다.




