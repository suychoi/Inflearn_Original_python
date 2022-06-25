'''
코루틴
 - 흐름제어, 병행성 처리
 - 메인루틴 <-> 서브루틴
 - 쓰레드 차이 설명
 - 제네레이터 -> 코루틴 설명

코루틴(Coroutine) : 단일(싱글) 스레드 환경에서 동시성 작업을 위한 프로그래밍 기법, Stack 기반으로 동작하는 비동기 작업

Thread : OS에서 관리하고, CPU코어에서 실시간, 시분할 비동기작업 : 멀티쓰레드

yield, send 키워드를 이용해서 : 메인루틴 <-> 서브루틴 : 간에데이터 교환 가능

코루틴 제어, 상태, 양방향 전송
서브루틴 : 메인루틴 호출 -> 서브루틴에서 수행(흐름제어)
코루틴 : 루틴 실행중 중지 -> 동시성 프로그래밍

코루틴 : 쓰레드에 비해 오버헤드 감소
쓰레드 : 싱글스레드 -> 멀티스레드 -> 복잡 -> 공유되는 자원의 교착상태 발생가능성 증가
        컨텍스트 스위칭 비용 발생, 자원 소비 가능성 증가. ★
'''

# 코루틴 EX1
def coroutine1():
    print('>> coroutine started.')
    i = yield
    print('>> coroutine received : {}'.format(i))

# yield가 들어가면 제네레이터이다. 코루틴은 제네레이터 기반으로 봄.

# 제네레이터 선언 / 메인 루틴 !!
cr1 = coroutine1()

print(cr1, type(cr1))

# yield 지점까지 서브루틴 수행
next(cr1)

# 기본 전달 값 None
# next(cr1)

# 값 전송
# cr1.send(100)  # 메인루틴과 서브루틴의 데이터 교환이 가능하다.

# 잘못된 사용법
# cr2 = coroutine1()
# cr2.send(100)       # yield 에서 멈추지 않고( =next 없이) send 를 보내는 경우.

print('-' * 60)

'''
Coroutine 상태값
 - GEN_CREATED : 처음 대기 상태
 - GEN_RUNNING : 실행 상태
 - GEN_SUSPENDED : Yield 대기 상태
 - GEN_CLOSED : 실행 완료 상태
'''
# 코루틴 EX2 Generator 기반으로 동시성 개발
def coroutine2(x):
    print('>>> Coroutine Started : {}'.format(x))
    y = yield x     #print(next(cr3)) 하면 여기까지 멈춰있음
    print('>>> Coroutine Received : {}'.format(y))
    z = yield x + y     #print(cr3.send(100)) 하면 여기까지 하고 멈춰있음
    print('>>> Coroutine Received : {}'.format(z))
    t = yield 'last'

cr3 = coroutine2(10)
from inspect import getgeneratorstate
print(getgeneratorstate(cr3))   #GEN_CREATED
print(next(cr3))
print(getgeneratorstate(cr3))   #GEN_SUSPENDED
print(cr3.send(100))
print(getgeneratorstate(cr3))   #GEN_SUSPENDED
print(cr3.send(101))

print('-' * 60)

'''
Python 3.5 이상에서, def -> async, 
                    yield -> await 으로 바꿔서 사용할 수 있음.
                    StopIteration 자동 처리(3.5 -> await) 
'''
# 코루틴 Ex3 중첩 코루틴 처리
def generator1():
    for x in 'AB':
        yield x
    for y in range(1,4):
        yield y

t1 = generator1()

print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
# print(next(t1))

t2 = generator1()
print(list(t2))

print('-' * 60)

def generator2():       # yield from 순차적으로 iterable 한것을 반환하는 것.
    yield from 'AB'
    yield from range(1,4)

t3 = generator2()
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
