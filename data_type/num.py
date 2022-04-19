"""
int, float, bool
complex : 복소수
str, list, tuple (시퀀스)
set(집합), dict: 사전
"""

dict = {
    'name': 'Machine Learning',
    "version": 2.0
}
print(dict)

list3 = [7, 8, 9]
tuple3 = (7, 8, 9)   # 7, 8, 9 로 선언도 가능하다. 
set3 = {7, 8, 9}

"""
+ - * / 
// 몫
% 나머지
abs(x) 절대값
pow(x, y)   x의y승
x ** y      x의y승
"""
a = 1.
b = 6
c = .7
d = 12.7
print(type(a), type(b), type(c), type(d))

#형변환
print(float(b))

print(abs(-7))
print()
#100을 8로 나눴을 때의 몫과 나머지
x, y = divmod(100, 8)
print(x, y)

print(pow(5, 3))

#외부 모듈
import math
print(math.pi)
print(math.ceil(3.7))   #올림

