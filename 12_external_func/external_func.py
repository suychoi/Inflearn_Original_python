# 전세계 파이썬 사용자들이 필요에 의해서 만든 기능들,
# 실제 프로그램 개발 중 자주 사용
# 종류 : sys, pickle, shutil, temfile, time, random 등

# 예제1
import sys
print(sys.argv) # 구글에 검색..? 이런속성값이 있다..! 나중에 심화에서 나올예정

# 강제 종료
# sys.exit()       강제종료 되기때문에 조심

# 파이썬 패키지 위치
print(sys.path)

# pickle : 객체 파일 쓰기
import pickle       # 클래스나 변수, 메소드, 파이썬의 자료형을 쓸 때 파일에 쓸 수 있다.!!
f = open("test.obj", "wb")
obj = {1 : 'python', 2 : 'study', 3 : 'basic'}
pickle.dump(obj, f)         # 쓸때는 dump
f.close()   # 열고나서 닫아줘야 합니다.
# 파이썬 객체를 저장했기때문에 사람이 읽기보단 파이썬으로 읽어야 합니다.

f = open('test.obj', 'rb')
data = pickle.load(f)       # 읽을 때는 load
print(data, type(data))
f.close()

# OS 관련 , 환경변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
# mkdir, rmdir( 비어있으면 삭제), rename
import os
print(os.environ)
print(os.environ["USERNAME"])

# 현재 경로
print(os.getcwd())

# time : 시간 관련 처리
import time

print(time.time())      #1653575405.0392404
print(time.localtime(time.time()))
#time.struct_time(tm_year=2022, tm_mon=5, tm_mday=26, tm_hour=23, tm_min=30, tm_sec=37, tm_wday=3, tm_yday=146, tm_isdst=0)

# 간단한 시간 표현
print(time.ctime())

# 가장 많이 사용될 형식
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))       # m = 월, M = 분

# 시간 간격 발생
for i in range(5):
    print(i)
    # time.sleep(2)

# random : 난수를 반환
import random
print(random.random())  # 0 ~ 1 실수 반환
print(random.randint(1,45))     # 1~ 45 사이에 난수
print(random.randrange(1, 45))  # 1~ 44 사이에 난수

# shuffle 섞기
d = [1,2,3,4,5,6,7]
random.shuffle(d)
print(d)

# 무작위 선택
c = random.choice(d)
print(c)

# webbrowser : 본인 OS의 웹브라우저를 실행하낟.
import webbrowser
webbrowser.open("http://google.com")
webbrowser.open_new("http://google.com")        # 새 창으로 열기

# pickle, time, os 많이 사용할거에용!~









