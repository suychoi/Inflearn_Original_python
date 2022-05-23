# 파이썬 예외처리의 이해,
# 예외 종류 : SyntaxError 문법에러, TypeError, NameError, IndexError, ValueError, KeyError ....
# 문법적으로 예외가 없지만, 코드 실행 단계(프로세스)에서 발생하는 예외도 중요하다.
# 1. 예외는 반드시 처리해야 한다.
# 2. 로그를 반드시 남긴다.
# 3. 예외는 던져진다. (다른곳으로 던져!)
# 4. 예외 무시 (비추천..)

# SynctaxError 문법 오류

# NameError 참조가 없을 때
import time

a = 10
# print(b)

# ZeroDivisionError
# print(100/0)      0 으로 나눌 수 없는 오류

# Index Error
X = [1, 2, 3]
# print(X[5])

# Key Error
dic = {'name' : 'kim', 'name2':'lee', "name3":'park'}
print(dic.get('name44'))    # key 가 없는 경우 발생, get으로 받아오면 에러 안나고 None으로 반환됨

# 완벽한 프로그램은 없다.
# 하지만 예외가 없는 것을 가정하고 프로그램을 작성해라 -> 그리고 런타임 예외 발생 시 예외처리 권장(EAFP)

# Attribute Error : 모듈, 클래스에 있는 잘못된 속성 사용 예외
import time
# print(time.time2())

# Value Error 참조값이 없는 경우
x = [10, 50, 90]
# x.remove(200)     자료구조 안에서 존재하지 않는 값을 참조하는 경우

# FileNotFound Error
# f = open('test.txt')

# TypeError : 자료형에 맞지 않는 연산을 수행하는 경우
x = [1, 2]
y = (1, 2)
z = 'test'
# print(x + y)
print(y[1])
# y[1] = 10

# 예외처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명 : 여러개 가능
# except TypeError
# else : try 블록에 에러가 없는 경우 실행됨.
# finally : 예외가 있든 없든 항상 마지막에 실행

name = ['kim', 'lee', 'park']

# 예제 1
try:
    z = 'lee'
    x = name.index(z)
except ValueError:
    # ValueError가 발생할 가능성이 크기때문에,,
    print('Not found! - Occurred ValueError~')
else:
    print('Found {}! {} in name'.format(z, x))
finally:
    print()

# 예제 2 Exception
try:
    z = 'cho'
    x = name.index(z)
except Exception:   #모든 에러를 잡지만 어떤 에러가 발생했는지는 모른다.
    print('Not found! - Error Occurred ')
else:
    print('Found {}! {} in name'.format(z, x))
finally:
    print()

# 예제 3
try:
    z = 'cho'
    x = name.index(z)
except Exception as e:   # 별명을 두고 예외에 대한 메시지를 볼 수 있다.
    print('Not found! - Error Occurred ')
    print(e)
else:
    print('Found {}! {} in name'.format(z, x))
finally:
    print()

# 예제 4
# 예외 발생 : raise
# raise 키워드로 예외를 직접 발생한다.
try:
    a = 'Park'
    if a == 'Kill':
        print('{} is kill'.format(a))
    else:
        raise ValueError
except ValueError:
    print('Exception occured')
else:
    print('Ok')
    # 파이썬의 문법에서의 에러가 아니라 기업이나 회사의 정책상에서 발생되는 에러에 사용.
