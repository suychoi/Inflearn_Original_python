"""
 - 해시 테이블
 - Immutable Dict 생성 ( 수정이 불가능 한 딕셔너리 생성!!)
 - 지능형 Set
 - Set 선언 최적화
"""
# 해시 테이블 -> 적은 리소스로 많은 데이터를 효율적으로 관리하기 위함
# Dict -> key 중복 허용 X
# Set -> 중복 허용 X
# Dict 및 Set 심화

# immutable Dict

from types import MappingProxyType
d = {'very_important_key' : 'value1'}   # 중요한 데이터인 경우, 수정이 안되도록 해줌.

# Read Only
d_frozen = MappingProxyType(d)      # read only 가 되며, 수정이 불가능함, frozen은 일종의 규칙
print(d, id(d))
print(d_frozen, id(d_frozen))       #hash(d_frozen) 지원하지 않음.

# 수정 가능
d['key2'] = 'value2'
print(d)

# 수정 불가
# d_frozen['key3'] = 'value3'

print('\n' * 3)

# Set

s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = {}
print(type(s4)) # 원소가 하나도 없을때는 set() 으로 선언해야 함.
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})      # 읽기전용으로 바꿔버린다.

s1.add('Melon')     # 데이터 추가 됨.
print(s1)
# s5.add('Melon')     # frozenset은 add가 안됨.

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 선언 최적화
# 파이썬은 실행시 바이트코드를 어셈블링해서 파이썬 인터프리터가 실행하는것임.
from dis import dis
# dis 는 바이트 코드 실행 순서 확인 가능하다.
# 논쟁! s1이 빠를까요 s2 가 빠를까요? 효율적인 코드를 작성하기 위해서는 차이를 아는게 중요하다.
# 그 차이를 증명해드림
print('-------------')
print(dis('{10}'))              # 과정이 더 짧은것을 확인
print('-------------')
print(dis('set([10])'))         # 5단계로 이뤄짐.
print('-------------')

# 지능형 집합(Comprehending set) 만들기
print('지능형 집합 생성')
from unicodedata import name
print({name(chr(i), '') for i in range(0, 256)})    # 키보드 자판 문자열로 변환해서.. name 함수로 없을때는 ''로 변환해줌.










