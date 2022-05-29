# 흐름 제어문( 04_if, 05_for, while )
# while 실습
# while <expr>:
#   <statement(s)>
# 조건에 만족하면 계속 반복

n = 5
while n > 0:
    print(n)
    n -= 1
# 무한반복이 될 수 있기 때문에 유의 해야 한다.

# 예제2
a = ['foo', 'bar', 'baz']
while a:
    print(a.pop())

# 예제3
# break, continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)

m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)

# while else 구문
# 중간에 break 가 없다면 조건문을 다 돌고 else 실행 됨.
x = 10
while x > 0:
     x -= 1
     print(x)
     if x == 5:
         break
else:
     print("else out")

# 예제 7
a = ['foo', 'bar', 'baz', 'qux']
s = 'qux'
i = 0
while i < len(a):
    if a[i] == s:
        print(a[i])
        break
    i += 1
else:
    print(s, 'not found')

#무한 반복은 조심해야 한다.
# while True:

while True:
    if not a:
        break
    print(a.pop())



