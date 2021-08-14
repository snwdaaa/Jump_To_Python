# 내장 함수
# import할 필요 X인 함수들
# 다 외울 필요 없고, 까먹었을 때마다 찾아보기

# abs(x) : x의 절댓값을 반환
print(abs(3))
print(abs(-3))
print(abs(-1.2))

print("=" * 30)

# all(x) : 반복 가능한 자료형 x를 인수로 받음. x가 모두 참이면 True, 하나라도 거짓이면 False
# 쉽게 말하면 False값이 하나라도 있는지 확인하는 함수
print(all([1,2,3]))
print(all([1,2,3,0])) # 0은 거짓, 0 이외의 수는 참이므로 False

print("=" * 30)

# any(x) : 하나라도 참이 있을 경우 True, 모두 거짓이면 False
# all(x) 함수의 반대
print(any([1,2,3]))
print(any([1,2,3,0]))
print(any([0,0,0]))

print("=" * 30)

# chr(i) : 아스키 코드값 i를 문자로 리턴
print(chr(65))
print(chr(97))

print("=" * 30)

# dir(x) : 객체 x가 자체적으로 가지고 있는 변수나 함수를 리스트 형태로 리턴
print(dir([1,2,3])) # 리스트 관련 함수, 변수들 출력
print(dir((1,2,3))) # 튜플 관련 함수, 변수들 출력

print("=" * 30)

# divmod(a, b) : a를 b로 나는 몫과 나머지를 튜플 형태로 리턴
print(divmod(7,3)) # (2,1)

print("=" * 30)

# enumerate(x) : 순서 있는 자료형(리스트, 튜플, 문자열) x를 입력으로 받아 인덱스 값을 포함하는 enumerate 객체 리턴
# enumerate 객체 : index와 요소의 이름을 가짐
# 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려주는 인덱스 값이 필요할 때 유용
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

print("=" * 30)

# eval(표현식) : 실행 가능한 문자열을 입력으로 받아 실행한 값을 리턴
print(eval('1+2')) # 3
print(eval("'hi'+'a'")) # 'hia'
print(eval('divmod(4,3)')) # '(1,1)'

print("=" * 30)