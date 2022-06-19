'''
 데코레이터(Decorator)
  - Closure -> Decorator 관계
  - 데코레이터 실습 1
  - 데코레이터 실습 2

  데코레이터 장점
  1. 중복 제거, 코드 간결, 공통 함수 작성
  2. 로깅, 프레임워크, 유효성 체크 -> 공통 기능으로 뽑음
  3. 조합해서 사용 용이

  데코레이터 단점
  1. 가독성 감소..?
  2. 특정 기능에 한정된 함수는 단일 함수로 작성하는 것이 유리할 수 있다.
  3. 디버깅 불편해짐
'''
# 데코레이터 실습
import time
def perf_clock(func):

    def perf_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()
        # 함수 실행
        result = func(*args)
        # 함수 종료 시간
        et = time.perf_counter() - st
        # 실행 함수명
        name = func.__name__
        # 함수 매개변수
        arg_str = ', '.join(repr(arg) for arg in args)      # generator 및 join
        # 결과 출력
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))
        return result
    return perf_clocked

# @perf_clock
def time_func(seconds):
    time.sleep(seconds)

# @perf_clock
def sum_func(*numbers):
    return sum(numbers)

# 데코레이터를 사용하지 않는 경우
none_decode1 = perf_clock(time_func)
none_decode2 = perf_clock(sum_func)
print(none_decode1, none_decode1.__code__.co_freevars)
print(none_decode2, none_decode2.__code__.co_freevars)
print()
none_decode1(1.5)
none_decode2(100, 200, 300, 400, 500)

print('-' * 100)

# 데코레이터를 사용하는 경우  @perf_clock 를 함수 위에 붙이면 됨

@perf_clock
def time_func(seconds):
    time.sleep(seconds)

@perf_clock
def sum_func(*numbers):
    return sum(numbers)
time_func(2.5)
sum_func(100, 200, 300, 400, 500)
