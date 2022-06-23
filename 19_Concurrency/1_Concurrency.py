'''
병행성(concurrency)
 - 병행성, 흐름제어 설명
 - 이터레이터(Iterator)
 - 제네레이터(Generator)
 - __iter__, __next__
 - 클래스 기반 제네레이터 구현

Python generators are a simple way of creating iterators.
All the work we mentioned above are automatically handled by generators in Python.
Simply speaking, a generator is a function that returns an object (iterator) which
we can iterate over (one value at a time).
'''

# 파이썬 반복 가능한 타입
# Collections, text file, list, Dict, Set, Tuple, unpacking, *args ... : iterable

t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print('__iter__' in dir(t))

for c in t:
    pass
    # print(c, end='')    #반복 확인

# 반복 가능한 이유 = 내부적으로 iter(x) 함수가 호출됐다.

# while
w = iter(t)     # iter 함수로 iter하게 만듦. 그 이후 next로 값 보기
# print(next(w))  #   A
# print(next(w))  #   B
# print(next(w))  #   C
# print(next(w))  #   D       다음 값을 기억함.

while True: # for 문의 원리는 이렇다. (예외처리도 됨)
    try:
        print(next(w))
    except StopIteration:
        break

# 반복형인지 확인
print(hasattr(t, '__iter__'))

from collections import abc
print(isinstance(t, abc.Iterable))  # Iterable 클래스를 상속 받았는지 확인.

# next를 이용해서 Iterable 한 Class 형태로 구현
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration.')       # raise ?
        self._idx += 1
        return word

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wi = WordSplitter('Do today what you could do tomorrow.')
print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print('-' * 30)
# Generator 패턴으로 하면 더 간편함.
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가 후 메모리 사용량 증가
#       그래서 제네레이터 사용을 권장
# 2. 단위 실행 가능한 코루틴(Coroutine) 구현과 연동
# 3. 작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word  # 제네레이터, 내부적으로 다음 반환될 값의 위치 정보를 기억함.
        return 'WordSplitGenerator(%s)' % (self._text)

wg = WordSplitGenerator('I can do this all day')
wt = iter(wg)
print(wt)   # wt : generator
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
# print(next(wt)) Error


#







