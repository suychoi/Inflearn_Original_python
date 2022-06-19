'''
클로저 심화(Closure)
 - 클로저 사용 예제
 - 잘못된 클로저 사용
 - 클로저 정리
'''
# 외부에서 호출된 함수의 변수값, 상태(Reference), 복사(snapshot) 후 저장 -> 후에 접근(Access) 가능

# Closure 사용, 패턴이 정해져있음
def closure_ex1():
    # Free variable 자유 변수
    # Closure 영역
    series = []
    def averager(v):
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager           # 일급함수의 특징, 함수 자체를 return 가능

avg_closure1 = closure_ex1()

print(avg_closure1) # 함수를 반환
print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))

print()

# 파이썬에서 Closure 의 속성을 확인
# function inspection
print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))       # co_freevars co가 붙은게 있음
print()
print(avg_closure1.__code__.co_freevars)
print()
print(avg_closure1.__closure__[0].cell_contents)
print('============================================')
## 잘못된 클로저 사용 예시
def closure_ex2():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        cnt += 1    # len
        total += v  # sum
        return total / cnt
    return averager

avg_closure2 = closure_ex2()
# print(avg_closure2(10))

print('============================================')
def closure_ex3():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total     # Free 변수로 만들어주는 키워드
        cnt += 1    # len
        total += v  # sum
        return total / cnt
    return averager

avg_closure3 = closure_ex3()
print(avg_closure3(10))
print(avg_closure3(30))
print(avg_closure3(50))

















