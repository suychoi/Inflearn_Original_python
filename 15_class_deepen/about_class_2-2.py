# 객체지향 프로그래밍 -> 코드의 재사용, 코드 중복 방지
# 규모가 큰 프로젝트(프로그래)이 과거에는 함수중심으로 코딩, 데이터가 방대해지고 복잡해졌다.
# 그래서 클래스 중심으로 코딩하도록 ( 데이터 중심 ) -> 객체로 관리된다.
# 클래스 중심은 언어의 문제가 아니다.
# 만들고자 하는 프로그램의 규모와 앞으로의 지향(목적)에 따라 클래스 기반이냐 절차 기반이냐를 고민해야 한다.


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

    def __str__(self):  #self 를 받으면 인스턴스 메서드 string
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self): #representation 객체를 그대로 자료형에 타입에따른 객체를 그대로 표시
        return 'repr : {} - {}'.format(self._company, self._details)

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))


car1 = Car('Ferrari', {'car_company' : 'Ferrari', 'car_detail' : {'color': 'White','horsepower': 400, 'price': 8000}})
car2 = Car('BMW', {'car_company' : 'BMW', 'car_detail' : {'color': 'Black', 'horsepower': 200,'price': 3000}})
car3 = Car('Audi',{'car_company' : 'Audi', 'car_detail' : {'color': 'Yellow', 'horsepower': 300, 'price': 4500}})

# 함수 호출
car1.detail_info()

# 비교
print(id(car1.__class__) == id(car2.__class__))

























