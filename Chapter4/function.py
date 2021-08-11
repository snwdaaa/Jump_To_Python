# 함수

# 1. 함수의 구조
def sum(a, b):
    return a + b



# 2. 입력값과 리턴값에 따른 함수의 형태
# a. 일반적인 함수 : 입력값이 있고, 리턴값이 있는 함수
def func1(a, b):
    result = a + b
    return result

# b. 입력값이 없는 함수
def func2():
    return 'Hi'

# c. 리턴값이 없는 함수
def func3(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

# d. 입력값, 리턴값 둘 다 없는 함수
def func4():
    print('Hi')



# 3. 입력값이 몇 개일지 모를 때
# 인수 부분의 변수를 ' *변수 ' 형태로 쓰기
# 그러면 인수로 입력된 모든 값을 튜플로 만든다

# 예제 : 여러 개의 입력값을 모두 더하는 함수
def sum_all(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum_all(1,2,3))


# 4. 함수의 결과값은 항상 하나
def func5(a, b):
    return a+b, a*b # 튜플

# 하나의 튜플값을 2개의 리턴값처럼 받고싶을 때
plus, mul = func5(3,4) # (7, 12)
print("%d %d" % (plus, mul))



# 5. 입력 인수에 초깃값 미리 설정하기
# 초깃값을 미리 설정한 변수에 입력값을 주지 않으면 그 변수는 초깃값을 갖게된다.
# 초기화시킬 인수는 항상 마지막에 위치해야한다.
def say_myself(name, age, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % age)
    
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

print(say_myself("a", 21, True))



# 6. 함수의 스코프
# 함수의 지역변수는 함수 밖에서 사용 X

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# a. return 이용
# b. global 명령어 이용
# global a => 함수 외부에 있는 변수 a를 함수 내부에서 직접 사용
# 외부에 의존하는 함수는 좋은 함수X이므로 global은 사용 자제
a = 1
def VarTest():
    global a
    a += 1
VarTest()
print(a)