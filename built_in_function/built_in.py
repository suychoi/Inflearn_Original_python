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

