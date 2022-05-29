#파이썬 변수
#기본 선언
n = 700
print(n)
print(type(n))

#동시선언
x = y = z = 800
print(x, y, z)

#Object Reference
# 변수의 값 할당 상태일 때 
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔에 출력

#Object의 ID의 확인, 객체의 고유값 확인
m = 800
n = 650

print(id(m))
print(id(n))
#는 각각 다르다.
print(id(m) == id(n))

#이름이 다른 변수에 같은 값이 있는 경우, ID는 같도록 한다.
#파이썬 인터프리터 일 잘하네
a = 800
b = 800
c = 800
d = 800
print(id(a) == id(b) == id(c) == id(d))


#다양한 변수 선언 방법
#camelCase : numberOfCollegeGraduates
    #method 생성 시 사용
#PascalCase : NumberOfCollegeGraduates
    #Class 생성 시 사용
#Snake_Case : number_of_college_graduates
    # 파이썬에서 사용, 소문자 중간에 언더바 삽입(파이썬에서 변수)


#예약어