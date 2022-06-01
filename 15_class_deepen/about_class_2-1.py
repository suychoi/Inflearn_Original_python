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

    # 사용자 레벨에서 print 로 정보를 확인할때는 __str__ 메서드를 구현
    def __str__(self):  #self 를 받으면 인스턴스 메서드 string
        return 'str : {} - {}'.format(self._company, self._details)

    # 개발자 레벨에서 텍스트 뿐만아니라 객체의 엄격한 정보를 확인할때는 __repr__ 메서드를 구현
    # __str__ 이 없으면 print(car1) 할 때 __repr__이 호출됩니다.
    def __repr__(self): #representation 객체를 그대로 자료형에 타입에따른 객체를 그대로 표시
        return 'repr : {} - {}'.format(self._company, self._details)

# Self 의미 : 인스턴스 메서드에서는 self가 첫번째 인자로 넘어오게 돼있다.


car1 = Car('Ferrari', {'color': 'White','horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'Black', 'horsepower': 200,'price': 3000})
car3 = Car('Audi',{'color': 'Yellow', 'horsepower': 300, 'price': 4500})

# ID 값 확인 다 다른것을 확인 -> 클래스는 하나지만, 인스턴스는 여러개다.
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)

# dir & __dict__
print(dir(car1))
print(dir(car1) == dir(car2))   #True

# 인스턴스의 namespace만 확인 딕셔너리 형태로 모든 값까지 보여준다.
print()
print(car1.__dict__)
print(car2.__dict__)


# Doctring 클래스에 정의된 코멘트 확인
print(Car.__doc__)
print()



























