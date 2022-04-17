#String 에서는 S를 생략해도 된다. 

# VSC 출력은 Ctrl + f5
#''' 따옴표3개도 가능합니다. 
print('''이게뭔데''')

# sep option
print('python', 'google.com', sep='@')

# End option(개행을 하지 않고 이어쓰기) Welcome to IT News Web Site
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

# file option
# 외부 파일에 출력내용을 저장한다. 
import sys
print('Learn Python', file=sys.stdout) 

#Format (d, s, f) 정수, 문자열, 실수
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', '2'))
# 인덱스 번호에 맞춰서 대입한다.
print('{1} {0}'.format('one', 'two'))

# %s 사용법 (10칸을 확보해두고  채운다.)
print('%10s' % ('nice'))    #("      nice")
print('{:>10}'.format('nice'))  #("      nice")

print('%-10s' % ('nice'))       #("nice     ")
print('{:10}'.format('nice'))   #("nice     ")

print('{:_>10}'.format('nice'))   #("______nice")
print('{:^10}'.format('nice'))   #("   nice    ")

#문자열의 크기가 더 큰 경우
# 마침표 기호가 있어야 잘린 상태로 출력된다. 
print('%.5s' % ('pythonstudy')) #("pytho")
#10공간 중에서 5공간만 출력
print('{:10.5}'.format('pythonstudy'))  #('pytho     ')


