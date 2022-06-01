"""
객체지향 프로그램은 코드의 재사용 + 중복을 방지한다.
규모가 큰 프로잭트에서 과거엔 함수중심으로 코딩이 되었고, 데이터가 방대해지고 복잡해졌다.
그래서 클래스 중심으로 코딩하도록 변했다. 데이터 중심에서 객체로 관리된다.

1. 절차지향
2. 객체지향
3. 함수형 프로그래밍 : 다른 방식으로 사고하는 방법을 적용한다.. !

이 수업은 일반적인 코딩 vs 데이터 자료구조를 활용한 코등 vs 클래스와 객체를 이용한 객체지향 코딩의
차이점을 느껴보고, 객체지향 프로그래밍의 기능을 느낀다.
"""
class Car():
    """
    잘만들어진 패키지를 보면 코멘트를 달아서 정의를 해준다.
    Car Class
    Author : suychoi
    Date : 2022-05-31
    """


    def __init__(self, company, details):
        self._company = company
        self._details = details

    # 사용자 레벨에서 print 로 정보를 확인할때는 __str__ 메서드를 구현
    def __str__(self):  #self 를 받으면 인스턴스 메서드 string
        return 'str : {} - {}'.format(self._company, self._details)

    # 개발자 레벨에서 텍스트 뿐만아니라 객체의 엄격한 정보를 확인할때는 __repr__ 메서드를 구현
    # __str__ 이 없으면 print(car1) 할 때 __repr__이 호출됩니다.
    def __repr__(self): #representation 객체를 그대로 자료형에 타입에따른 객체를 그대로 표시
        return 'repr : {} - {}'.format(self._company, self._details)

car1 = Car('Ferrari', {'car_company' : 'Ferrari', 'car_detail' : {'color': 'White','horsepower': 400, 'price': 8000}})
car2 = Car('BMW', {'car_company' : 'BMW', 'car_detail' : {'color': 'Black', 'horsepower': 200,'price': 3000}})
car3 = Car('Audi',{'car_company' : 'Audi', 'car_detail' : {'color': 'Yellow', 'horsepower': 300, 'price': 4500}})

# print(car1.__init__())
print(car1.__str__())
print(car1.__repr__())

print(car1.__dict__)
print(dir(car1))
print(car1 is car2)
print(Car.__doc__)
