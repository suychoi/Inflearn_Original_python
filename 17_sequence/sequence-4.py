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






