# for문

# for문의 기본 구조
# for 변수 in 리스트(or 튜플, 문자열)
#   수행할 문장 ...
# 리스트(or 튜플, 문자열)의 첫 번째 요소부터 마지막 요소까지 '변수'에 대입된다

# for문 예제
# 예제 1. 전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i) # test_list에 있는 모든 요소가 첫 번째부터 마지막까지 변수 i에 차례대로 대입된다.

# 예제 2. 다양한 for문의 사용
# 대입되는 변수의 형태는 리스트(or 튜플, 문자열)의 형태와 같아야한다.
a = [(1,2), (3,4), (5,6)]
for (first, last) in a: # 대입하는 변수를 튜플로 받음. 형태가 다르면 오류 발생
    print(first + last)

# 예제 3. for문의 응용
# 학생 5명, 60점 넘으면 합격, 아니면 불합격. 결과 보여주기
marks = [90, 25, 67, 45, 80]
number = 0 # 학생에게 붙여줄 번호
for mark in marks:
    number += 1

    if (mark >= 60): print("%d번 학생은 합격입니다." % number)
    else: print("%d번 학생은 불합격입니다." % number)


# continue문
# 60점 이상인 사람에게는 축하 메시지를 보내고, 아니면 아무 것도 하지 않는 예제
marks = [90, 25, 67, 45, 80]
number = 0 # 학생에게 붙여줄 번호
for mark in marks:
    number += 1

    if (mark < 60): continue # 다음 순서로 건너 뜀
    print("%d번 학생 축하합니다. 합격입니다." % number)


# for문과 range 함수 (매우 중요)

# range 함수 -> 숫자 리스트를 자동으로 만들어주는 함수
# 시작 숫자와 끝 숫자를 지정하려면 range(시작숫자, 끝숫자) 형태로 사용. 이때 끝 숫자는 포함 X
a = range(10) # 0부터 10 미만의 숫자를 포함하는 range 객체를 만든다.
print(a)
b = range(0, 10)
print(b)

# for문과 range 함수의 조합 예시
# 1부터 10까지 더하는 예제
sum = 0
for i in range(1, 11):
    sum+=i
print(sum)

# 점수 예제 - range 함수 응용
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % (number + 1))

# 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('') # 파이썬의 print 함수는 자동으로 줄바꿈 한다는 것을 이용


# 리스트 안에 for문 포함하기 -> 리스트 내포(List Comprehension)
# 리스트 내포의 일반적 문법
# [표현식 for 항목 in 반복가능객체 if 조건]

# a 리스트의 각 요소에 3을 곱한 결과를 다른 리스트에 저장하기
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)

# 짝수에만 3을 곱하기 -> 리스트 내포 if 조건
result = [num * 3 for num in a if (num % 2 == 0)]
print(result)

# 리스트 내포 2중 for문
result = [x * y for x in range(2,10)
                for y in range(1,10)]
print(result)