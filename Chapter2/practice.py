# 연습문제

# 문자열

# 1. 주민등록번호를 연월일 부분과 그 뒤의 숫자 부분으로 나누어 출력
pin = "881120-1068234"
yyyymmdd = pin[:6] # 881120
num = pin[7:]
print(yyyymmdd) # 연월일 부분 출력
print(num) # 숫자 부분 출력

print('-' * 20)

# 2. 주민등록번호에서 성별을 나타내는 숫자를 출력
pin = "881120-1068234"
print(pin[7])

print('-' * 20)

# 리스트

# 1. [1,3,5,4,2]를 [5,4,3,2,1]로 만들기
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

print('-' * 20)

# 2. ['Life', 'is', 'too', 'short'] 라는 리스트를 Life is too short라는 문자열로 출력
a = ['Life', 'is', 'too', 'short']
result = ' '
print(result.join(a))

print('-' * 20)

# 튜플

# 1. (1,2,3) 튜플에 4 추가
a = (1,2,3)
a = a + (4,)
print(a)

print('-' * 20)

# 딕셔너리

# 1. 딕셔너리 a에서 'B'에 해당하는 값을 추출하고 삭제
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

print('-' * 20)

# 집합

# 1. a 리스트에서 중복된 숫자 제거
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

print('-' * 20)