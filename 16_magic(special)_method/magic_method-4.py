'''
컴퓨터 공학에서 객체(Object) = 클래스에서 정의한 것을 토대로 메모리(실제 저장공간)에 할당된 것
    프로그램에서 사용되는 데이터 or 식별자에 의해 참조되는 공간을 의미한다.

Magic(Special) Method :
사용자 정의 함수 외에, 사용자 정의 클래스에서 내장된 python 함수를 사용하는 것
'''

class Fruit():
    def __init__(self, _name, _price):
        self.