'''
파이썬 일급함수(객체)
 - 파이썬 함수 특징
 - 익명함수(Lambda)
 - Callable 설명
 - Partial 사용법

일급함수(객체)는 함수형 프로그래밍을  가능하게 한다.

파이썬 함수 특징
 1. 런타임 초기화
 2. 변수 할당 가능
 3. 함수 인수 전달 가능
 4. 함수 결과 반환 가능(return)
'''

# 팩토리얼 함수 객체
def factorial(n):
    '''Factorial Function -> n : int'''             # n이 int를 받는다.
    if n == 1: # n < 2
        return 1
    return n * factorial(n-1)

class A:
    pass

# 객체취급 증명
print(factorial(5))
print(factorial.__doc__)    # 함수 코멘트 출력
print(type(factorial), type(A))     # factorial 함수를 객체로 취급함.
print(dir(factorial))   # 클래스가 아니고 함수지만 객체 취급을 한다.
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))        # 함수만 갖고있는 성질들 출력
#{'__defaults__', '__globals__', '__get__', '__qualname__', '__kwdefaults__', '__closure__', '__name__', '__code__', '__call__', '__annotations__'}
print(factorial.__name__)   #  함수의 이름
print(factorial.__code__)

print('\n' * 2)

# 파이썬 함수 특징 증명, 1. 변수 할당 증명
var_func = factorial        # factorial() 은 실행하는 것, factorial 은 할당만 하는 것
print(var_func)
print(var_func(10))     # 변수에 할당한 상태로 함수 실행 가능
print(list(map(var_func, range(1, 11))))

# 2. 함수로 인수 전달 및 함수로 결과 반환 -> 고위 함수(higher-order function)
# map, filter, reduce 3종 세트는 중요합니다. !!!
# javascript es6 에서도 나옵니다. (프론트에서 나온다는 뜻)
print('\n' * 2)
print([var_func(i) for i in range(1,6) if i % 2])   # 홀수의 팩토리얼만 출력
print(list(map(var_func, filter(lambda  x: x % 2, range(1,6)))))    # 다르지만 같은 결과
# var_func 함수를 lambda 함수로 전달함. lambda 함수도 익명함수인데 filter 함수의 인자로 전달됨.

print()

# reduce 함수
from functools import reduce
from operator import add

print(sum(range(1,11)))
print(reduce(add, range(1, 11)))    # range(1, 11) 이 실행되면서 하나하나를 줄여가면서 누적해서 더해줌...!

# 익명함수 ( lambda )
# 람다는 가급적 주석을 꼭 작성하라! , 더 가급적 함수로 만들어라!
# 일반 함수 형태로 리팩토링을 권장!

print(reduce(lambda  x, t: x + t, range(1,11))) # x 와 t를 받아서 함. 누적하면서 더함

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# 호출 가능한지 확인
print(callable(str), callable(list), callable(var_func), callable(factorial), callable(3.14))    # 호출이 가능하면 True
# 3.14 는 상수라서 false가 나옴.

# partial 사용법 : 인수 고정 -> 콜백 함수에 사용
from operator import mul
from functools import partial
print()
print(mul(10, 10))  # 하나의 10 을 고정하는 경우
five = partial(mul, 5)  # 일급객체니까 함수를 인수로 전달 가능.
print(five(10))     # mul(5, 10)
print(five(100))

# 고정 추가
six = partial(five, 6)
print(six())        # 이미 2개의 인자, 5,6 을 받아서 계산됨.

print([five(i) for i in range(1,11)])       # 5의 배수
print(list(map(five, range(1,11))))


















