"""
 - 해시 테이블(Hashtable)
 - Dict 생성 고급 예제
 - Setdefault 사용법
"""

# 해시 key가 중복되면 어떻게 처리하는지?

# 해시 테이블
# : Key 에 Value를 저장하는 구조, 파이썬 자체가 hash table engine으로 구성.

# 파이썬 dict 해쉬테이블 예
# key 값의 연산 결과에 따라 직접 접근이 가능한 구조이기 때문에 사용. 고유한 값을 찾아가는 이점이 있음.
# 파이썬에서는 hash를 구현할 필요가 없다. dict를 사용하면 된다.
# key 값을 해싱 함수 -> 해쉬 주소 가 나옴 -> 기반으로 key에 대한 value 의 위치를 참조

# Dict ( 해쉬 테이블 구조 확인)
# print(__builtins__.__dict__)        # 'print': <built-in function print>, 'repr': <built-in function repr>

# hash 값 확인, 고유성 확인!

t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
# print(hash(t2))     # TypeError: unhashable type: 'list' 값이 변경되는 list이기 때문에 hash가 안됨.
# 즉 hash함수는 불변형 데이터타입을 받을 수 있음.
print('\n' * 3)

# Dict Setdefault 예제, tuple에서 dict 만들때 권장하는 방법.
# source 라는 튜플을 dict로 바꾸는 예시
source = (('k1', 'val1'),
            ('k1', 'val2'),
            ('k2', 'val3'),
            ('k2', 'val4'),
            ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use Setdefault 랑 Use Setdefault 경우 비교
# No use Setdefault
for k, v in source:
    if k in new_dict1:      # key가 이미 있는지 확인
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

# Use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)    #{'k1': ['val1', 'val2'], 'k2': ['val3', 'val4', 'val5']}

# 주의사항
new_dict3 = {k: v for k, v in source}
print(new_dict3)        # key가 덮어씌워진다. 이렇게 사용하면 안됨.



