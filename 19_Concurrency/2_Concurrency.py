'''
병행성(Concurrency)
 - 제네레이터 실습
 - Yield 실습
 - Itertools 실습

병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행
                    -> 단일 프로그램안에서 여러일을 쉽게 해결
병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행
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
# count, takewhile,  filterfalse, accumulate, chain, product, groupby ...
print()
import itertools
gen1 = itertools.count(1, 2.5)  # 무한대의 값을 만들어줌. 1 부터 2.5 간격으로 높아짐
print(next(gen1))
print(next(gen1))
print(next(gen1))

# 조건
gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))

for v in gen2:
    # print(v)
    pass

# filter 반대
print()
gen3 = itertools.filterfalse(lambda n : n < 3, [1,2,3,4,5]) # 3미만의 값을 제외하고 반환

for v in gen3:
    print(v)

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1,101)])
for v in gen4:
    print(v)    # 5050 까지 나옴. 누적되어 계산함.

# 연결1
gen5 = itertools.chain('ABCDE', range(1,11,2))  # 서로 다른 iterable 을 묶음
print(list(gen5))

# 연결2
gen6 = itertools.chain(enumerate('ABCDE'))  # index 번호를 붙여줌.
print(list(gen6))

# 개별
gen7 = itertools.product('ABCDE')
print(list(gen7))

# 개별
gen8 = itertools.product('ABCDE', repeat=2)     # 다양한 경우의 수로 묶어줌
print(list(gen8))

# 그룹화
gen9 = itertools.groupby('AAABBCCCCDDEEE')
# print(list(gen9))
for chr, group in gen9:
    print(chr, ' : ', list(group))  # 중복되는 문자열을 걸러내는

# iterrable 한 데이터에 관련된 메서드들!


