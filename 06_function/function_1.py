# 파이썬 함수의 중요성
# 함수 식 및 람다(lambda)

# 함수 정의 방법
# def function_name(parameter):
#   code

#예제 1
def first_func(w):
    print("Hello,", w)

word = "good boy"
first_func(word)

# 예제 2
def return_func(w1):
    value = "Hello, " + str(w1)
    return value

x = return_func('Good girl')
print(x)

# 파이썬은 함수형 프로그래밍
# 기존의 위에서 아래로 작성하는 명령형이나 절차식 프로그래밍에서
# 함수형 프로그래밍을 이용하면 더 많은 장점이 있음. 일반(명령형에 비해서)

# 다중 반환 예제
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3       # 다중 반환

# 받는 쪽도 언팩킹으로 알아서 받도록
v1, v2, v3 = func_mul(10)
print(v1, v2, v3)

def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)       # 튜플로 묶어서 반환(리스트나 집합도 가능)

q = func_mul2(20)
print(type(q), q)

def func_mul3(x):       # 딕셔너리 형태의 반환
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'x1':y1, 'x2':y2, 'x3':y3}
d = func_mul3(30)
print(type(d), d)
print(d.get('x1'), d['x2'])
print(d.items())
print(d.keys())
print(d.values())

# *, **:
# 중요

# *args(언팩킹)
# 몇개의 어떤 변수가 와도 언팩킹해서 풀어서 사용하게 해줄게
# 가변인자에 대해 사용이 가능하도록 해준다.
def args_func(*args):    # 매개변수 명 자유
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print("-----------")

args_func("Lee")    #   Result : 0 Lee
args_func("Lee", 'Park', 'Choi')    #   Result : 0 Lee
# Result : 0 Lee
# Result : 1 Park
# Result : 2 Choi

# **kwargs(언팩킹)     #dictionary 키:값 의 데이터를 넘길때 사용한다.
def kwargs_func(**mm): # 매개변수 명 자유
    for v in mm.keys():
        print("{}".format(v), mm[v])
    print('-----')

kwargs_func(name1='Lee', name2='Choi', name3='Park')

# 전체 혼합
# 알아서 언패킹 하는것..!! 대단하다.
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)
example(10, 20, 'Lee', 'Choi', 'Cho', age1=20, name1="susu")

#중첩 함수
# 함수형 프로그래밍과 연관된 내용 클로저, 1급 객체..!!?
def nested_func(num):
    def func_in_func(num):  #함수안에 함수는 호출되어야
        print(num)
    print("In func")
    func_in_func(num + 100)
nested_func(100)
# func_in_func 함수내부의 함수는 단독으로 호출될 수 없다.

#람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결,
# 지금 예제에서는 람다식을 간편하게 사용하는 것만 보여준다.
# 일반적인 함수는 객체 생성 -> 리소스(메모리)에 할당 하는 절차를 밟고,
# 람다는 즉시 실행 함수이기 때문에 Heap 영역에 저장이 되고 -> 그 이후에 메모리 초기화가 된다.

# 함수 vs 람다식, 무엇이 더 좋은지 결정은 내가 하는것.
# 함수는 이름으로, 람다식은 무명함수라서 변수에 할당해서 사용.
def lam_func(x, y):
    return x * y

print(lam_func(10, 50))
mul_func_var = lam_func
print(mul_func_var(20, 50))

lambda_mul_func = lambda  x, y:x*y    #변수:리턴
print(lambda_mul_func(50,50))

#이름이 필요없이 그 자리에서 간편하게 사용할 수 있는 함수
def func_final(x, y, func):
    print('>>>>>>>', x * y * func(100, 100))

func_final(10, 20, lambda x,y:x * y)
func_final(10, 20, mul_func_var)
# 함수 안에 함수를 넣을때, lambda 식을 사용해도 되고,
# 일반 함수를 넣어도 된다.












