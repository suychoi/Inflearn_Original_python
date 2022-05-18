# 파이썬에서 사용자 입력
# 런타임에서 데이터를 입력받는 것
# Input 사용법

# 예제1
# name = input("Enter your name :")
# grade = input("Enter your grade :")
#
# print(name, grade)

#예제 2
# number = input("Enter number : ")
# print(type(number))
# 기본타입은 무조건 문자열(str)로 들어온다.

# first_num = int(input("Enter num1 "))
# second_num = int(input("Enter num2 "))
# print("num1 + num2 = ", first_num + second_num)

#예제 4
float_num = float(input("Enter float num : "))
print(float_num)
print(type(float_num))

#Print 에서 바로 입력을 받는 문법
# format 함수 ?! 복습 필요하다. 
print("FirstName - {0}, LastName - {1}".format(input("Enter first name : "), input("Enter second name : ")))



