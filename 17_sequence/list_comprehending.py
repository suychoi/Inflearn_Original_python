'''
지능형 리스트( List Comprehension):
'''

result = []
for i in range(10):
    result.append(i)
print(result)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result2 = [_ for _ in range(10)]
print(result2)

# 0~9 의 값 중 짝수만 있는 리스트 생성
result3 = [i for i in range(10) if i % 2 == 0]
print(result3)

# 0~2, 0~2 의 데카르트 곱의 결과를 가진 리스트의 생성..?
result4 = [i * j for i in range(3) for j in range(3)]
print(result4)

# 0~2 의 값 중 2일 경우를 찾아 곱한 값을 가지고 있는 리스트의 생성
result5 = []
for i in range(3):
     if i == 2:
          for j in range(3):
               if j == 2:
                    result5.append(i * j)
print(result5)

result6 = [i * j for i in range(3) if i == 2 for j in range(3) if j == 2]
print(result6)
