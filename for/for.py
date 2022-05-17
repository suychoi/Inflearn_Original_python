#파이썬 반복문
#For 실습

#for in <collection>        #list tuple dictionary 등 집합의 형태(다수의 데이터)
#   <Loop body>

for v1 in range(10):
    print('v1 is', v1)

print()

for v2 in range(1, 11):
    print('v2 is', v2)

for v3 in range(1, 11, 2):  #1 부터 2씩 뛰면서 10까지
    print('v3 is', v3)

#쉽게 숫자의 합 구하기
print('1~1000 의 합은', sum(range(1, 1001)))
print('1~1000 에서 4배수의 합은', sum(range(0, 1001, 4)))

# Iterables 자료형 반복(반복이 가능한)
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

#예제1
names = ['Kim', 'Park', 'Cho', 'Lee']
for n in names:
    print(n)

# 예제 2
word = "Beautiful"
for s in word:
    print(s)
# 예제 3 dictionary
my_info = {
    "name": "Lee",
    "Age": 33,
    "City": "Seoul"
}
for key in my_info:
    # print(key, my_info[key])
    print(key, my_info.get(key))
# 예제 4
name = 'PineApPle'
for w in name:
    print(w.upper())


#Break 문 (불필요한 반복문에서 탈출)
num = [1, 16, 100, 64, 23,73, 24, 43,78]
for num in num:
    if num == 16:
        print("num is ", num)
        break
    else:
        print("no!")

#Continue   부득이하게 bool 형을 제외하는 경우 사용
lt = ["1", 2, 5, True, 4.3, complex(4)]
for v in lt:
    if type(v) is bool:  #자료형 비교는 is
        continue
    print("current type : ", v, type(v))

# for - else 구문!!
num = [1, 16, 100, 64, 23,73, 24, 43,78]
for v in num:
    if v == 99:
        print("Found", v)
        break
else:
    print(99, "not found")

#구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i*j), end='')
    print()

# 변환 예제
name2 = "Aceman"
print('Reversed', reversed(name2))
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Sets', set(reversed(name2)))











