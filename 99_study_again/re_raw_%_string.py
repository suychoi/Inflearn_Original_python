'''
01 format_function

%d , %f, %s 참고

# %d print 함수에서 %d 는 정수의 포멧 대치 함수다.
크게 %d 를 사용하거나, {} 를 사용한다.
'''

print('%d' % (3))
print(' %d %d' % (4, 5))
print('{} {}'.format(1, 3))

print('%4d' % (32))
print('%30d' % (32))

print('%f' % (3.145))
print('%14f' % (3.145))

print('{:f}'.format(3.1234))

#정수 한자리와, 소수 5자리까지 출력
print('%1.5f' % (3.13123451523523535315))
print("{:f}".format(6.12345152352353))

# 003.14 총 6자리에서 소수 2자리가 나오도록 함
print('%06.2f' % (3.12312451235125))
print('%099.2f' % (3.12312451235125))

'''
String 에서는 S를 생략해도 된다. 

'''

print('python', 'google.com', sep='@')
print('백설기', '일곱난장이', sep='와 ')

# End option :  개행을 하지 않고 이어쓰기
print('Well', end=' ')
print('Come', end=' ')
print('to', end=' ')
print('Hell', end=' ')

# file option
# 외부 파일에ㅐ 내용을 출력 저장.
import sys
print('I \'m learning python now.', file=sys.stdout)

# format option
print('%s %s' % ('one', 'two'))
print('{1} {0}'.format('one', '2'))