#문자열은 중요하다.

"str 은 중요하다!"
#빈 문자열 할당
str_t1 = ''
str_t2 = ""
str_t3 = str()

# Escape 문자
print("I'm man")
#print('I'm man")
print('I\'m man') # \ 를 사용해서 문자로 사용
print(' \t ')       # tab key
print(' \n ')       # 줄바꿈 key
print(" \"kimchi wow!\"")

#Raw String     # r 을 이용해서 \ 를 문자그대로 사용, 파일 경로 사용시 사용
raw_s1 = r'D:\python\test'
print(raw_s1)

#멀티 라인 입력 \ 를 사용해서 멀티라인 입력
multi_str = \
"""
12345
678901
234567
89123
456789
"""
print(multi_str)

#문자열의 연산 [ + * in ]
str_o1 = "Python is Hard"
print("y" in str_o1)
print('z' not in str_o1)


#문자열의 형변환
#눈에 보이는건 int 지만, type은 str 이다. 
print(str(66), type(str(66)))

#문자열 함수(upper, isalnum, startwith, count, endwith, isalpha .....)
str_f = 'python'
print("Capitalize :", str_f.capitalize()) #Python 맨 첫글자를 대문자로
print("endswith :", str_f.endswith("n")) #맨 끝문자 확인
print("replace :", str_f.replace('n', 'n is good!'))
#replace : python is good!

print("sorted: ", sorted(str_f))
#sorted:  ['h', 'n', 'o', 'p', 't', 'y']

print("split: ", str_o1.split(' '))
#split:  ['Python', 'is', 'Hard']

#시퀀스 순서가 있는 배열 형태
im_str = "Good boy!"
# print(dir(im_str))
#dir 함수를 사용하면 __iter__ 을 사용해서 시퀀스를 할 수 있다...??????

#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', 
# '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 
# 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


#슬라이싱
str_s1 = "Nice Python"
print(len(str_s1))
print(str_s1[0:3]) #Nic 
print(str_s1[5:]) # 끝까지 가져와 Python
print(str_s1[:])    # 처음부터 끝까지가져와
print(str_s1[1:4:2]) #ie 1부터 4까지 2씩 커지면서 가져와라
print(str_s1[-5:]) #음수의 경우 끝부터 시작 ython 

#아스키 코드
a = "z"
print(ord(a)) # 122 z의 아스키코드
print(chr(122)) # 아스키코드 -> 문자