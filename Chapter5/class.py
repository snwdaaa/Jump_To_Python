# 1. 클래스 기초
class Service:
    secret = "영구는 배꼽이 두 개다." # 클래스 변수

    # __init__ 함수는 인스턴스를 만들 때 항상 실행된다.
    def __init__(self, name):
        self.name = name


    def SetName(self, name):
        # self는 인스턴스가 되고, name은 주어진 변수가 되므로
        # a.name = "A" 가 된다.
        self.name = name     

    # 클래스 함수
    # self : 클래스의 인스턴스가 맞는지 확인하기 위한 변수
    # 클래스 함수를 인스턴스에서 호출하기 위해서는 무조건 첫 번째 인수에 self가 있어야 함
    # 호출이 발생하면 self는 호출 시 이용했던 인스턴스로 바뀌게 됨 (매우 중요)
    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s입니다." % (self.name, a, b, result))

# __init__ 함수에 의해, 인스턴스를 선언할 때, 필요한 값을 입력해야 한다.
a = Service("A")

print(a.secret) # 클래스 변수 사용
# a.SetName("A")
print(a.sum(1,1))



# 2. 클래스 자세히 알아보기
# 클래스에 의해 생성된 객체들은 다른 객체들과 완전히 다른 저장 공간을 가지고 독립적으로 동작한다.

# a. 사칙연산 클래스 만들기
class FourCal:
    # 클래스 함수 = 메서드(Method)
    # SetData 함수는 FourCal 클래스의 메서드
    def SetData(self, first, second):
        # 각각 개체의 변수는 이름은 같아도, 다른 저장공간에 있는 서로 다른 변수임
        self.first = first
        self.second = second

    def Sum(self):
        result = self.first + self.second
        return result

    def Mul(self):
        result = self.first * self.second
        return result

    def Sub(self):
        result = self.first - self.second
        return result

    def Div(self):
        result = self.first / self.second
        return result

b = FourCal()
b.SetData(4, 2)
print(b.Sum())
print(b.Mul())
print(b.Sub())
print(b.Div())


# b. 박씨네 집 클래스 만들기
# 박씨 가족의 이름을 설정하고(SetName), 가족 중 한 사람이 여행 가고싶은 곳을 출력(Travel)
class HousePark:
    lastName = "박"

    def __init__(self, name):
        self.SetName(name)

    def SetName(self, name):
        self.fullName = self.lastName + name

    def Travel(self, location):
        print("%s, %s여행을 가다." % (self.fullName, location))

    def Love(self, other):
        print("%s, %s와 사랑에 빠졌네" % (self.fullName, other.fullName))

    def Fight(self, other):
        print("%s, %s 싸우네" % (self.fullName, other.fullName))

    # 연산자 오버로딩(Overloading) : 객체끼리 연산을 할 수 있게 한다.
    # 객체끼리 연산을 할 때 특정 함수가 호출된다.
    # __add__ : 객체끼리 덧셈할 때 호출된다.
    # __sub__ : 객체끼리 뺄셈할 때 호출된다.
    # __mul__ : 객체끼리 곱셈할 때 호출된다.
    # __truediv__ : 객체끼리 나눗셈할 때 호출된다.
    def __add__(self, other):
       print("%s, %s와 결혼했네" % (self.fullName, other.fullName))

    def __sub__(self, other):
        print("%s, %s 이혼했네" % (self.fullName, other.fullName))
    

a = HousePark("A") # __init__ 함수를 사용할 경우, 객체를 생성할 때 입력값을 줌
print(a.lastName)
print(a.fullName)
a.Travel("부산")

# 클래스 상속(Inheritance)
# HousePark 클래스를 상속해 HouseKim 클래스 만들기
# 클래스를 상속할 떄는 class 클래스이름(상속할 클래스 이름) 형태로 적어준다.
class HouseKim(HousePark):
    lastName = "김"

    # Method Overriding
    # 자식 클래스에서 부모 클래스의 메서드와 이름은 같되, 추가적이거나 다른 동작을 하게 하는 것
    def Travel(self, location, days):
        print("%s, %s여행 %s일 가다." % (self.fullName, location, days))

b = HouseKim("B")
print(b.lastName)
print(b.fullName)
b.Travel("독도", 3)

a.Love(b)
a + b # 연산자 오버로딩

pey = HousePark("응용")
juliet = HouseKim("줄리엣")
pey.Travel("부산")
juliet.Travel("부산", 3)
pey.Love(juliet)
pey + juliet # 연산자 오버로딩
pey.Fight(juliet)
pey - juliet # 연산자 오버로딩
