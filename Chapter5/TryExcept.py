# try, except, else, finally, pass, raise

# 예외 처리

# 1. 자주 발생하는 오류

# a. FileNotFoundError : 디렉토리 안에 없는 파일을 열려고 할 때 발생
# b. ZeroDivisionError : 0으로 다른 숫자를 나누는 경우 발생
# c. IndexError : 최대, 최소 인덱스를 넘는 인덱스를 참조했을 때 발생

# 2. 오류 예외 처리 기법

# a. try, except문
# try 블록 수행 중 오류가 발생하면 except 블록 실행
# 오류가 발생하지 않으면 except문 무시
"""
try:
    # ...
except [발생 오류]:    -> 이때 []는 적어도 되고, 생략해도 된다는 표기법. 괄호[]를 쓰는건 아님
    # ...
"""

# except 사용법
# try, except만 쓰기 -> 오류 종류에 상관없이 오류가 발생하면 except 블록 실행
"""
try:
    # ...
except:
    # ...
"""
# 발생 오류만 포함한 except문 -> except문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록 실행
"""
try:
    # ...
except 발생 오류:
    # ...
"""
# 발생 오류, 오류 메시지 변수까지 포함한 except문 -> 위의 방법에서 오류 메시지의 내용까지 알고싶을 때 사용
"""
try:
    # ...
except 발생 오류 as 오류 메시지 변수:
    # ...
"""

# 예
try:
    4 / 0
except ZeroDivisionError as e:
    print(e) # division by zero 출력


# b. try .. else
# else 절은 예외가 발생하지 않은 경우에 실행
# 반드시 except절 바로 다음에 위치해야 함

# foo.txt라는 파일이 있으면 else절 수행, 없으면 except절 수행
try:
    f = open('foo.txt', 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    f.close()


# c. try .. finally
# finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행
# 대개 사용한 리소스를 close할 때 자주 사용
# f = open('foo.txt', 'w')
# try:
    # ~~
# finally:
    # f.close()


# 3. 오류 회피하기
# 특정 오류를 통과시킬 수 있다
# except 문에서 pass를 사용해 오류를 회피하도록 할 수 있다.
try:
    f = open('나없는파일', 'r')
except FileNotFoundError:
    pass # 오류 회피
except IndexError:
    pass


# 4. 오류 발생시키기
# raise 발생 오류 -> 해당 오류를 강제로 발생시킨다.

# 예
# 클래스를 상속받는 자식 클래스가 특정 함수를 반드시 구현하도록 만들기
class Bird:
    def Fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def Fly(self):
        print("very fast")

eg = Eagle()
eg.Fly()