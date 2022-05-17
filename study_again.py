#Escape 문자
print("I'm man")
print('I\'m man')
print('a \t b')
print('a \n b')
print(" \"kimchiman\" ")

#Raw String
raw_string = r'D:\python\test'
print(raw_string)

#멀티 라인 입력
multi_line = \
"""
this letter is from
USA
and the writer is
suychoi
"""
print(multi_line)

test_s1 = "Python is Hard"
print("y" in test_s1)


#문자열 함수( upper, isalnum, startwith, count, endwith, isalpha ... )
test_s2 = "python"
print("Capitalize : ", test_s2.capitalize())    # 맨 첫 문자를 대문자로
print("endswith : ", test_s2.endswith('n'))     # 맨 마지막 문자 확인
print("replace : ", test_s2.replace('n', 'n is good!'))
print("sorted: ", sorted(test_s2))
print("split :", test_s1.split(' '))

# dir 메서드로 __iter__ 을 사요해서 시퀀스가 가능하다
# print(dir(test_s1))

#슬라이싱
test_s3 = 'Nice Python'
print(len(test_s3))
print(test_s3[0:3])
print(test_s3[5:0])
print(test_s3[:])
print(test_s3[1:4:2])
print(test_s3[-5:])

#아스키 코드 변환
a = "z"
print(ord(a))   # z 의 아스키 코드
print(chr(122)) # 아스키 코드 -> 문자


# 다양한 변수 선언 방법
# camelCase : numberOfCollegeGraduates
#     method 생성 시 사용
# PascalCase : NumberOfCollegeGraduates
#     Class 생성 시 사용
# Snake_Case : number_of_college_graduates
#     파이썬에서 사용, 소문자 중간에 언더바 삽입(파이썬에서 변수)

