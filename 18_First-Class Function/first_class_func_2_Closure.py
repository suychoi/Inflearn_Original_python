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
    global c        # global 키워드를 사용하면 글로벌 변수로 사용 가능
    print(a)
    print(c)        # 밑에 지역변수 c 가 할당돼있지만, 글로벌 변수 선언을 해놨기 때문에 정상 동작한다.
    c = 40
    print()

print('before', c)
func_v4(10)
print('after', c)            # func_v4 에서 40 으로 재할당된 c 의 값을 확인할 수 있다.