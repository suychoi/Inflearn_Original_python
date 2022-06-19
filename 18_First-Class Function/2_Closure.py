'''
클로저 기초(Closure)
 - 파이썬 변수 범위(Scope)
 - Global 선언
 - 클로저 사용 이유
 - Class -> Closure 구현
'''

# 파이썬 변수 범위(Scopre)
# 지역변수와 전역변수의 차이를 알고있어야 함.
def func_v1(a):
    print(a)
    print(b)

b = 20

def func_v2(a):
    print(a)
    print(b)

func_v2(10)
# 메모리 관리 생명주기? GC의 lifecycle
print()

c = 33333

def func_v3(a):
    print(a)
    print(c)        # 로컬 변수와 글로벌 변수가 동시에 있는 경우, 로컬변수가 참조전에 할당되지 않으면 오류가 발생한다.
    # c = 40
    print()

func_v3(10)


def func_v4(a):
    global c        # global 키워드를 사용하면 글로벌 변수로 사용 가능 / 함수 내 지역변수와 글로벌 변수가 얽히면 좋은 코딩 방법이 아니다.
    print(a)
    print(c)        # 밑에 지역변수 c 가 할당돼있지만, 글로벌 변수 선언을 해놨기 때문에 정상 동작한다.
    c = 40
    print()

print('before', c)
func_v4(10)
print('after', c)            # func_v4 에서 40 으로 재할당된 c 의 값을 확인할 수 있다.

# Closure 는 기억한다! 함수의 참조가 끝나도 값을 기억한다.
# Closure 를 사용하는 이유는, 서버 프로그래밍에서 동시성(Concurrency) 제어를 위해서 즉,
# 같은, 한정된 메모리 공간에 여러 자원이 접근하여,
# 교착상태( Dead Lock) 를 해결하기 위해서!

# 메모리를 공유하지 않고 메시지 전달로 처리하기 위한 개념에서 클로저가 나옴...! Erlang ?
# Closure는 공유하되, 변경되지 않는(Immutable, Read only) 성질을 적극적으로 사용함.
# Closure는 함수형 프로그래밍하고 연결됨.

# 결론 : Closure는 불변 자료구조 및 atom, STM 을 통해서 멀티스레드(Coroutine) 프로그래밍에 강점을 제공함.
# 단일 스레드 환경에서도 멀티 스레드인것처럼 환경을 조성 하기 위해 클로저를 배움.
# 클로저는 불변상태를 기억한다.

print('-------------------------------------------')
a = 100
print(a + 100)
print(a + 1000)
# a 의 값을 누적해서 계산하기 위해서는 ...
print(sum(range(1, 51)))
print('-------------------------------------------')

# 클래스를 이용해서 상태값 누적
class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

# 인스턴스 생성
averager_cls = Averager()
print(dir(averager_cls))        # call 함수 존재
print(averager_cls(10))
print(averager_cls(30))
print(averager_cls(50))
print(averager_cls(70))
print(averager_cls(182))        # 누적되는 효과, 클로저의 개념과 비슷.
















