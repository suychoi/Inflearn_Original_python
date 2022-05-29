# 데이터 과학에서 많이 사용하는 csv,
# 파이썬은 내부적으로 csv 파일에 관한 기능을 제공해줌
# csv 파일 형식을 알아놓아야 합니다. 데이터 전처리 시 사용하기도 합니다.

# CSV : MEME - text/csv (마임타입, csv 타입으로 통신을 해야한다는 의미)

import csv
# 원래는 (,) 로 구분하는게 정석이다.
with open("../00_resource/test.csv", 'r') as f:
    reader = csv.reader(f)
    next(reader)    # Header Skip 커서를 한줄 내림
    #객체 확인
    print(reader)
    print(type(reader))
    print(dir(reader)) #__iter__ 있음
    print()

    # 05_for c in reader:
        # print(c)  # 리스트로 받아온다.
        # print('|'.join(c))

with open('../00_resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')      # 구분자 !!
    # 05_for c in reader:
        # print(','.join(c))
        # print(c)

# 딕셔너리로 만들기
with open('../00_resource/test.csv', 'r') as f:
    reader = csv.DictReader(f)
    # 객체 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    for c in reader:
        # print(c)
        for k,v in c.items():
            print(k, ":", v)
        print("--------------------")       # DICT 형태로 csv 파일을 가져오면 이렇게 사용 가능!

w = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18], [19,20,21]]
with open('../00_resource/write1.csv', 'w', encoding='UTF-8') as f:
    print(dir(csv))
    wt = csv.writer(f)
    print(dir(wt))
    print('__iter__' in dir(wt))
    print(type(wt))

    for v in w:     # 의 내용을 하나씩 wt에 쓰는것
        wt.writerow(v)

with open('../00_resource/write2.csv', 'w', encoding='UTF-8') as f:
    # 필드명
    fields = ['One', 'Two', 'Three']    # 헤더로 사용할것
    # Dict Writer
    wt = csv.DictWriter(f, fieldnames=fields)
    wt.writeheader()
    # Header Write 여기까지 헤더 이름가 내부적으로 작성된 상태(1번 줄에)
    # 내용 작성
    for v in w:
        wt.writerow({'One': v[0], 'Two': v[1], 'Three': v[2]})

# 서로 다른 데이터 타입을 짧은 코드로 변환하고 읽고 쓰기 때문에 Data Science에서 유용하게 사용하는 것입니다.!