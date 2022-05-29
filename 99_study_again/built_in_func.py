
# enumerate : 인덱스 + 반복가능한 객체 반환
for i , name in enumerate(['abc', 'bcd', 'efg']):
    print(i + 1, name)

# filter : 반복가능한 객체 요소를
# 지정한 함수 조건에(True) 맞는 값만 추출

def conv_pos(x):
    return abs(x) > 7
print(list(filter(conv_pos, [1, 2, 3, 4, 5])))

print(list(filter(lambda x: abs(x) > 2, [-1, -2,-3,-4,-5,-6])))

# map : 반복 가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)
print(list(map(conv_abs, [-1, -2,-3,-4,-5,-6])))
print(list(map(lambda x: abs(x), [-1, -2,-3,-4,-5,-6])))
