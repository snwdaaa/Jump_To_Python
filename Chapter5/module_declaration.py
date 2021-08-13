# 모듈 만들기

def Sum(a, b):
    return a + b

def SafeSum(a, b):
    if type(a) != type(b):
        print("더할 수 있는 것이 아닙니다.")
        return
    else:
        result = a + b
    return result

# 변수, 클래스를 포함한 모듈
PI = 3.141592

class Math:
    def Solve(self, r):
        return PI * (r ** 2)


# __name__ == "__main__"인지 확인하면
# 다른 파일에서 import당할 때 실행되는 것을 막을 수 있다.
# 즉, 자기 자신이 실행된 것이 아니면 실행하지 않겠다는 의미
if __name__ == "__main__":
    print(SafeSum(1,2))
    print(Sum(1,2))