'''
병행성(Concurrency)
 - 제네레이터 실습
 - Yield 실습
 - Itertools 실습

병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행
                    -> 단일 프로그램안에서 여러일을 쉽게 해결
병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행행
                    -> 분업, 속도
'''

# Generator ex1

def generator_ex1():
    print('Start')
    yield 'A Point '    # return 의 역할
    print('Continue')
    yield 'B Point '
    print('End')

temp = iter(generator_ex1())
# print(next(temp))
# print(next(temp))

for v in generator_ex1():   # yield 키워드로 반복가능하게 만들어줌
    # print(v)
    pass

# Generator ex2
temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())    # temp3 는 Generator 임... 왜?

print(temp2)    # yield 가 return의 역할을 해줌.
print(temp3)    # <generator object <genexpr> at 0x0000015308757A50>

for i in temp3:
    print(i)

# Generator Ex3( 중요 함수)
# filterfalse, accumulate, chain, product, groupby ...




