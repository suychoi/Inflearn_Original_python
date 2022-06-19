'''
클래스 상세 설명
 - 클래스 변수 vs 인스턴스 변수
 - 클래스 메소드 실습
 - 네임 스페이스 이해
'''

class Car():
    """
    잘만들어진 패키지를 보면 코멘트를 달아서 정의를 해준다.
    Car Class
    Author : suychoi
    Date : 2022-05-31
    """

    # Class 변수 ( 클래스 변수는 모든 인스턴스가 공유 )
    car_count = 0

    def __init__(self, company, details): #인스턴스 변수는 _ 언더바를 앞에 붙이는 약속이 있기도 하다. (약속!!)
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self):  #self 를 받으면 인스턴스 메서드 string
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self): #representation 객체를 그대로 자료형에 타입에따른 객체를 그대로 표시
        return 'repr : {} - {}'.format(self._company, self._details)

    def __del__(self):
        print("del 메서드 호출됨")
        Car.car_count -= 1

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))


car1 = Car('Ferrari', {'color': 'White','horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'Black', 'horsepower': 200,'price': 3000})
car3 = Car('Audi',{'color': 'Yellow', 'horsepower': 300, 'price': 4500})

# 함수 호출
car1.detail_info()

# 비교, 부모의 Class 정보는 같다.
print('Class compare -------------------')
print(id(car1.__class__) == id(car2.__class__))
print()

# 에러
Car.detail_info(car3)   # class로 접근하면 self 인자를 전달해줘야 합니다.
# Car.detail_info()
#TypeError: detail_info() missing 1 required positional argument: 'self'

# 클래스 변수 공유 확인
print('\n', '클래스 변수 공유 확인')
print(car1.car_count)       # 클래스 변수를 직접 가져올 수는 있느데
print(car1.__dict__)        # __dict__ 메서드로 읽어오면 클래스변수는 같이 안읽어진다..!
print(dir(car1))            # dir로 접근하면 클래스 변수까지 확인이 가능하다.

# 접근
print(car1.car_count)
print(Car.car_count)        # 클래스 변수는 클래스로 접근하는게 더 정석이다.
print()

# def 삭제 메서드
del car2
print(Car.car_count)

# print(car2.__dict__)

# 인스턴스 네임스페이스에 없으면 상위에서 자동으로 검색한다.
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스변수, 부모클래스 변수)에서 찾는다. )
# 인스턴스에서 클래스 변수와 동일한 이름의 변수를 생성하면, 인스턴스 변수를 먼저 찾는다. (우선시한다.)





















