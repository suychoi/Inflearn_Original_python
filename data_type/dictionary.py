# json 형태랑 비슷한 가장 많이 사용될 타입.
# Key=Value 형태로 저장, Java에서는 Map이라고 한다.
#순서가 없다, 키 중복허용X, 수정가능, 삭제 가능
#선언 상당히 다양한 방법으로 선언 가능하다.
# (튜플)
# [리스트]
# {딕셔너리}    중괄호

#선언   a = {'KEY': 'Value'}
a = {'name': 'Kim', 'phone': '01012341234', 'birth': '870415'}
b = {0: 'HELL Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'Niceman',
    'City': 'Seoul',
    'Age': 33,
    'Status': True
}
#dict() 안에 리스트 안에 튜플형태로 한줄한줄 입력해도 딕셔너리 선언이 된다.
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Status', True)
])
## 가장 사용하기 편할듯
f = dict(
    Name='Niceman',
    City='Seoul',
    Age=33,
    Grade='A',
    Status=True
)

print(type(a),a)
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f),f)
print()
# 키 출력
print(a['name'])
# print(a['name1'])  KeyError: 'name1'
# [ ] 방식으로 키를 가져오면 키가 없는 경우 에러가 발생, 아래의 .get 방식으로 가져오는게 더 안전하다.
print(a.get('name1'))   # 키가 없으면 None으로 반환
print(b.get(0))
print(f.get('City'))

#딕셔너리 추가는 속성값으로 접근
a['address'] = 'seoul'
print(a)
a['rank'] = [1, 2, 3]
print(a)

print(len(a)) # Key의 개수를 반환

#딕셔너리에서 지원하는 함수
# dict_key, dict_values, dict_items : 반복문에서 사용 가능
print(a.keys())
print(b.keys())
print(c.keys())
print(d.keys())
print(list(f.keys()))
print()
print(a.values())
print(b.values())
print(c.values())
print()
print(a.items())
print(b.items())    #dict_items([(0, 'HELL Python')]) 리스트 안에 튜플 형태로 반환
print(c.items())
print()
print(a)
print(a.pop('name'))    #pop 으로 꺼내오면 반환하면서 삭제된다.
print(a)

print(f)
print(f.popitem())      #임의로 하나의 값을 pop 한다.
print(f)

print('birth' in a)     # 딕셔너리 안에 key가 있는지 확인함.
print('birth2' in a)

a['test'] = 'test_dict'
print(a)
a.update(test='test_man')
print(a)
test = {'test': 'Pusan'}        #명시적으로 선언하고 업데이트 해줘도 된다.
a.update(test)
print(a)

