# 객체지향 프로그래밍 -> 코드의 재사용, 코드 중복 방지
# 규모가 큰 프로젝트(프로그래)이 과거에는 함수중심으로 코딩, 데이터가 방대해지고 복잡해졌다.
# 그래서 클래스 중심으로 코딩하도록 ( 데이터 중심 ) -> 객체로 관리된다.
# 클래스 중심은 언어의 문제가 아니다.
# 만들고자 하는 프로그램의 규모와 앞으로의 지향(목적)에 따라 클래스 기반이냐 절차 기반이냐를 고민해야 한다.

# 일반적인 코딩 ...

#차량 1
car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color' : 'White'},
    {'horsepower' : 400},
    {'price' : 8000}
]
#차량 2
car_company_2 = 'BMW'
car_detail_2 = [
    {'color' : 'Black'},
    {'horsepower' : 200},
    {'price' : 3000}
]
# 차가 늘어날수록 길어진다.

#차량 3
car_company_3 = 'Audi'
car_detail_3 = [
    {'color' : 'Yellow'},
    {'horsepower' : 300},
    {'price' : 4500}
]

# 리스트 구조를 사용함. 관리하기가 불편, 인덱스 접근시 실수 가능성, 삭제 불편
car_company_list = ['Ferrari', 'BMW', 'Audi']
car_detail_list = [
    {'color': 'White','horsepower': 400, 'price': 8000},
    {'color': 'Black', 'horsepower': 200,'price': 3000},
    {'color': 'Yellow', 'horsepower': 300, 'price': 4500}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)
print(type(car_detail_list[1]))
print()
print()

# 딕셔너리 구조로 만들면!
# 코드 반복 지속, Key 중첩 문제가 있다. 키 조회 예외 처리 등
car_dicts = [
    {'car_company' : 'Ferrari', 'car_detail' : {'color': 'White','horsepower': 400, 'price': 8000}},
    {'car_company' : 'BMW', 'car_detail' : {'color': 'Black', 'horsepower': 200,'price': 3000}},
    {'car_company' : 'Audi', 'car_detail' : {'color': 'Yellow', 'horsepower': 300, 'price': 4500}}
]
print(car_dicts)

del car_dicts[1]
# key 삭제시 pop으로 ~
print(car_dicts)

# 클래스 구조로 만드는 경우!
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Car():
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

print(car1)
print(car2)
print(car3)
print()

print(car1.__dict__)    # 딕셔너리 형태로 클래스 내부에 속성값 확인
print(car2.__dict__)
print(car3.__dict__)
print()

print(dir(car1))
print()

# 리스트 선언
car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

for i in car_list:
    print(i)    # 반복문에선 str이 호출됨.
    print(repr(i))      # repr이 호출됨
# str : Ferrari - {'car_company': 'Ferrari', 'car_detail': {'color': 'White', 'horsepower': 400, 'price': 8000}}
# str : BMW - {'car_company': 'BMW', 'car_detail': {'color': 'Black', 'horsepower': 200, 'price': 3000}}
# str : Audi - {'car_company': 'Audi', 'car_detail': {'color': 'Yellow', 'horsepower': 300, 'price': 4500}}

