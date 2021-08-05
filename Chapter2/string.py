# 문자열 (인덱싱, 슬라이싱, 포매팅)

# 파이썬에서 문자열 만드는 네 가지 방법
"Hello World" # 큰따옴표 사용
'Python is fun' # 작은따옴표 사용
"""Hello Python""" # 큰따옴표 3개 사용
'''Hello Python''' # 작은따옴표 3개 사용

# 문자열 안에 따옴표 포함하기
# 작은따옴표를 포함하려면 큰따옴표로 둘러싸고, 큰따옴표를 포함하려면 작은따옴표로 둘러싼다.
food = "Python's favorite food is perl" # 작은따옴표 포함 -> 큰따옴표로 둘러싸기
print(food)
say = '"Python is very easy." he says' # 큰따옴표 포함 -> 작은따옴표로 둘러싸기
print(say)

# 백슬래시를 이용해 문자로 인식
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says"
print(food)
print(say)



# 여러 줄의 문자열을 변수에 대입하기
# 1. 줄바꿈 이스케이프 코드 '\n' 사용
multiLine = "Life is too short\nYou need Python" # 읽기 불편하고, 줄이 길어짐
print(multiLine)

# 2. 연속된 따옴표 3개 이용 -> 깔끔함
multiLine = """
Life is too short
You need Python
"""
multiLine = '''
Life is too short
You need Python
'''
print(multiLine)



# 문자열 연산하기
# 1. 문자열 더하기 -> 문자열을 덧셈 기호로 연결(concatenate)할 수 있다.
head = "Python"
tail = " is fun!"
print(head + tail)

# 2. 문자열 곱하기 -> 문자열의 반복
str_multiply = "python"
print(str_multiply * 2)



# 문자열 인덱싱 & 슬라이싱
# 1. 문자열 인덱싱 -> 문자열[index]는 문자열 내 index번의 문자를 가져옴
str = "Life is too short, You need Python"
print(str[3]) # 'e' 출력
# 인덱싱 활용
# a. - 기호를 붙이면 문자열의 뒤에서부터 시작한다.
print(str[-2]) # 'o' 출력

# 2. 문자열 슬라이싱
print(str[0:4]) # 'Life' 출력. str[시작번호:끝번호]에서 끝번호는 포함되지 않는다.
print(str[19:]) # 끝번호를 생략하면 시작번호부터 문자열의 끝까지 뽑아낸다.
print(str[:17]) # 시작번호를 생략하면 문자열의 처음부터 끝번호까지 뽑아낸다.
print(str[:]) # 시작번호와 끝번호를 모두 생략하면 문자열 처음부터 끝까지 뽑아낸다.
print(str[19:-7]) # - 기호 사용 가능

# 슬라이싱으로 문자열 나누기 예제
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date + " " + weather)



# 문자열 포매팅
# 1. 숫자 바로 대입
print("I eat %d apples." % 3)

# 2. 문자열 바로 대입
print("I eat %s apples." % "five")

# 3. 변수 대입
number = 3
print("I eat %d apples." % number)

# 4. 2개 이상의 값 대입
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days" % (number, day))

# 5. 문자열 정렬
print("%10s" % "hi")
print("%-10s" % "hi")

# 6. 소수점 표현하기
print("%0.4f" % 3.42134234) # 소수점 네 자리까지만 나타냄



# 문자열 관련 함수
# 1. 문자 개수 세기 -> 문자열.count('문자') : 문자열 안에 인수로 입력된 문자의 개수를 리턴
a = "hobby"
print(a.count('b'))

# 2. 위치 알려주기1 -> 문자열.find('문자') : 문자열 안에 인수로 입력된 문자가 처음으로 나오는 인덱스를 리턴
a = "Python is best choice"
print(a.find('b')) # 문자열에서 b가 처음으로 나온 위치의 인덱스를 반환
print(a.find('k')) # 존재하지 않는다면 -1 반환

# 3. 위치 알려주기2 -> 문자열.index('문자') : 문자열 안에 인수로 입력된 문자가 처음으로 나오는 인덱스를 리턴
print(a.index('b'))
    # find 함수와 다른 점은 문자가 없으면 오류가 발생한다.

# 4. 문자열 삽입 -> 문자열A.join('문자열B') : 인수로 입력된 문자열B의 각 문자들 사이에 문자열A를 삽입한다.
a = ","
print(a.join("abcd"))

# 5. 소문자 -> 대문자 => 문자열.upper()
a = "hi"
print(a.upper())

# 6. 대문자 -> 소문자 => 문자열.lower()
a = "HI"
print(a.lower())

# 7. 왼쪽 연속된 공백 지우기 => 문자열.lstrip()
a = " hi "
print(a.lstrip())

# 8. 오른쪽 연속된 공백 지우기 => 문자열.rstrip()
a = " hi "
print(a.rstrip())

# 9. 양쪽 연속된 공백 자우기 => 문자열.strip()
a = " hi "
print(a.strip())

# 10. 문자열 바꾸기 => 문자열.replace("바뀔 문자열", "바꿀 문자열")
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# 11. 문자열 나누기
# 문자열.split() : 공백을 기준으로 문자열 나눔
# 문자열.split('문자') : 문자를 기준으로 문자열 나눔
# 나뉜 값들은 리스트 형태로 리턴
a = "Life is too short"
print(a.split())
a = "a:b:c:d"
print(a.split(':'))
