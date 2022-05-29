# module = 연관 관계가 있는 변수, 클래스, 함수 등이 모아져있는 파일(기능 단위)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

# import 시 바로 실행되는 문제가 있음
# print('-' * 20)
# print('called! inner!')
# print(add(5,5))
# print(subtract(10,5))
# print(multiply(5,3))
# print(divide(10,2))
# print(power(10,2))
# print('-' * 20)

# __name__ 키워드 사용,
if __name__ == "__main__":  #다른 곳에서 호출하면 실행이 안되도록 한다.
    print('-' * 20)
    print('called! __main__!')
    print(add(5,5))
    print(subtract(10,5))
    print(multiply(5,3))
    print(divide(10,2))
    print(power(10,2))
    print('-' * 20)