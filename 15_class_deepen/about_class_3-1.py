'''
클래스 기반 메소드 심화
 - Class Method
 - Instance Method
 - Static Method
 - 3가지 메소드 활용 실습
'''

class Car():
    """
    잘만들어진 패키지를 보면 코멘트를 달아서 정의를 해준다. print(Car.__doc__)
    Car Class
    Author : suychoi
    Date : 2022-06-01
    Description : Class, Static, Instance Method
    """

    # Class 변수 ( 클래스 변수는 모든 인스턴스가 공유 )
    price_per_raise = 1.0   # 자동차 과세 비율

    def __init__(self, company, details):       # 인스턴스 변수는 _ 언더바를 앞에 붙이는 약속이 있기도 하다. (약속!!)
        self._company = company
        self._details = details

    def __str__(self):  #self 를 받으면 인스턴스 메서드 string
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self): #representation 객체를 그대로 자료형에 타입에따른 객체를 그대로 표시
        return 'repr : {} - {}'.format(self._company, self._details)

    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용(고유함)
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    # 가격의 전 후를 반환해주는 인스턴스 메서드 생성
    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # class method
    @classmethod                     #
    def raise_price(cls, per):       # class method는 cls를 인자로 받습니다. cls = Class
        if per <= 1:
            print("Please Enter 1 Or More")
            return
        cls.price_per_raise = per
        print('Price raised succeesfully!')

    # Scatic Method     클래스 메서드보다 유연하게 사용할 수 있는 메서드, 아무런 인자도 받지 않는다.
    @staticmethod
    def is_bmw(inst):   # 인스턴스가 bmw인지 확인하는 메서드
        if inst._company == 'BMW':
            return "This car is {}".format(inst._company)
        return 'Sorry. This car isn\'t BMW'


car1 = Car('Ferrari', {'color': 'White','horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'Black', 'horsepower': 200,'price': 3000})

# 전체 정보 출력
car1.detail_info()
car2.detail_info()

# 가격정보 직접 출력 , 메서드 미 사용
print(car1._details.get('price'))
print()
# 이렇게 직접 인스턴스 변수에 접근하는거는 좋지 않아서 privite 로 막아놓죠?
# 대신 메소드를 만들어서 필요로하는 정보만 반환을 하죠

# 메서드로 가격정보 접근( 인상 전 가격정보)
print(car1.get_price())
print(car2.get_price())
print()

# 인상 후 가격정보
Car.price_per_raise = 1.4       # 클래스변수도  직접접근해서 변경하는건 좋지 않아요 -> 클래스 메서드를 만들어서 접근!
# 메서드로 인상 후 가격 반환
print(car1.get_price_culc())
print(car2.get_price_culc())

# 클래스 메서드로 가격인상
Car.raise_price(1)
print()
Car.raise_price(1.1)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 스태틱 메서드 확인
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
print(Car.is_bmw(car1)) # 클래스로 호출해도 된다..!!! 그래서 유연하다.











