# 모듈 사용 실습
# 모듈이 모여서 패키지가 된다.
import sys

print(sys)  # built-in
print(sys.path)
# 위 경로 안에서 내가 만든 모듈, 또는 패키지를 검색한다. 파이썬의 원리

print(type(sys.path))
print(len(sys.path))
for i in range(len(sys.path)):
    path = sys.path
    print(path[i])

#모듈 경로 추가 (C:\math)     # 영구적이지 않음
# sys.path.append('C:\math')
# print(sys.path)

# import test_module
#print 함수가 자동으로 불려짐;; 이러면 안되요! -> 방지 하는 방법은  __name__ 키워드 사용

# print(test_module.power(10, 3))

import  python_module
# __name__ 키워드 사용 하면,
print(python_module.add(5,5))