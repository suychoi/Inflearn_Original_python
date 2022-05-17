#Sets
#data 분석
#집합은 순서 X, 중복X

# 선언
a = set()
print(type(a))
#빈 set([원소 ]) 안에 리스트 형태로 요소를 넣어 선언
b = set([1, 2, 3, 4])
c = set([1, 2, 'Pen', 'cap', 'plate'])
# 중괄호 선언에서 key=value 형태로 선언을 하지 않는 경우 Sets가 된다.
e = {'foo', 'bar', 'baz', 'foo'}    #중복허용을 안한다.

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(e, type(e))

#튜플 변환
t = tuple(b)
print(t, type(t))

#리스트 변환
l = list(b)
print(l, type(l))
print(e)
print(len(e))

#집합 연산
s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5, 6, 7, 8])

print("교집합! = ", s1 & s2)
print(s1.intersection(s2))

#합집합
print("합집합 = ", s1 | s2)
print(s1.union(s2))

#차집합
print("차집합 = ", s1 -s2)
print(s1.difference(s2))

#중복되는 원소가 없는지 true / false 확인
print(s1.isdisjoint(s2))  #False 가 나오면 교집합이 존재한다.

#부분집합인지 확인하는 메서드
print("subset : ", s1.issubset(s2))  #전체가 포함되는 관계가 아니다.
print("superset : ", s1.issuperset(s2))

#데이터 추가 제거
s1 = set([1, 2, 3, 4])
print(s1)
s1.add(5)       #요소 추가
print(s1)
s1.remove(5)    #요소 삭제, 요소가 없는 경우 에러
print(s1)
s1.discard(7)   #요소가 없어도 에러가 안납니다.
# 없는 요소를 remove로 삭제하는 경우 에러가 나기 때문에
# discard 함수로 삭제해야 합니다.
s1.clear()      #요소 전부 삭제제
print(s1)
