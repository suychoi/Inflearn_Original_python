# 리스트 선언, 특징, 인덱싱, 슬라이싱, 함수, 삭제

#순서가 있고 중복도 가능하고 수정도 가능하고 삭제도 가능한 아이!!
#선언
a = []
print(type(a))
b = list()
c = [1, 2, 3, 4]
print(len(c))
d = [1000, 10000, 'Ace', 'Base', 'Captain']
e = [1000, 10000, ['Ace', 'Base', 'Captain']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱
print('d - ', type(d), d)
print('d -', d[1])
print('d -', d[0] + d[1] + d[1]) # int 형을 인식하고 자동으로 저장한다.
print('e - ', e[-1][1])
print(list(e[-1][1])) #String 문자열은 시퀀스입니다.

#슬라이싱
print('d -', d[0:2])
print('e -', e[-1][1:3])

# list 연산
print(c + d) # append 된다.
print(c * 3)
# print('test + c[0] = ', 'test' + c[0] ) #type Error
print('test + c[0] = ', 'test' + str(c[0] )) #test1

#값 비교
print(c == c[:3] + c[3:])

# Identity(id) check
temp = c
print(temp, c)
print(id(temp) == id(c)) # 같은 ID 값을 갖고있습니다.
print(id(temp[1]) == id(c[1])) # 요소도 같은 하나의 주소값을 공유합니다.

print(c[0])
c[0] = 888
print(c[0])
print(c) #[888, 2, 3, 4]
c[1:2] = ['a', 'b', 'c']    # 리스트끼리 슬라이싱 연산은 요소가 더해진다.
print(c)
c[1] = ['zzz', 'zz', 'z']   # 직접 대입하는 경우, 리스트 자체가 들어간다.
print(c)
c[:4] = []
print(c)

# 제거
del c[0]    #[3, 4]
print(c)    #[4]
print("======================================================================")
#리스트 함수
a = [5, 4, 3, 2, 1]
print('a', a)
a.append(10)
print('a', a)
a.sort()
print('a', a)
a.reverse()     #뒤집기
print('a', a)

print(a.index(1))

a.insert(2, 7) # 2번 인덱스에 7을 삽입
print(a)
# del a[6]
a.remove(10) # 값을 이용해서 제거
print(a)

print(a.pop()) #끝에있는 원소를 반환하고 제거
print(a)
print(a.pop())
print(a)

print(a.count(1))   #1의 요소 수가 몇 개 들어가 있는가? 혹은 유무를 확인
ex = [1, 2]
a.extend(ex)
print(a)
a.sort()
while a:
    data = a.pop()
    print(data)