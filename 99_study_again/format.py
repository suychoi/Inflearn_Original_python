#String 에서는 S 를 생략해도 된다.

print(''' your name ''')
print('python', 'google.com', sep="@")

print('Welcome to', end=' ')
print('IT News', end='AA')
print('Web Site')

print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', '2'))
print('{1} {0}'.format('one', 'two'))

print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice')) #______nice
print('{:^10}'.format('nice'))  #   nice   #




















