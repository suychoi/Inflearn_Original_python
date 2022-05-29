
#파이썬 제어구문
# 04_if !
#True 를 나타내는 것, 0이 아닌 숫자, 'abc', {1,2,3}, (1,2,3...) 있는 경우 True
#False 를 나타내는 것, 0 이나 비어있는 "", [] {} () 같은건 False입니다.

#파있썬은 들여쓰기가 중요하다.
if "":
    print("best")
elif "1":
    print('im ture')
a, b, c = 10, 20, 30
print('and : ', a > b and b < c)
print('or : ', a > b or b < c)
print('not : ', not a > b)      # 결과값의 반대로 나온다.

# 산술, 관계, 논리의 우선 순위는
#1. 산술
#2. 관계
#3. 논리

print("e1 : ", 3+5 < 3+6)   # 산술(+) 먼저 실행, 그 후 관계 (<) 시행
print("e2 : ", 5 + 10 > 3 and 7 + 3 == 10)  #True and True 로 True

#예시
id1 = "vip"
id2 = "admin"
role = "gold"

if id1 == "vip" or id2 == "admin":
    print("관리자 권한 부여")
elif id2 == "admin" and role == "gold":
    print("최상위 관리자!")

#다중 조건문
#in 과 not in
q = [10, 20, 30]
w = {70, 80, 90, 100}   #Sets
e = {"name":"Lee", "City":"Seoul", "Grade":"A"}
r = (10, 12, 14)

print(15 in q)
print("name" in e)
print("Seoul" in e.values())    #값 안에서 찾기
