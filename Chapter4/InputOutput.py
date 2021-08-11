# 입력과 출력

# 1. 입력

# a. input 사용
# input은 입력되는 모든 것을 문자열로 취급
"""
a = input()
print(a)
"""

# input에서 프롬프트 띄우기
# input의 인수로 문자열 입력
"""
b = input("b의 값을 입력하세요: ")
print(b)
"""



# 2. 출력

# print의 특징
# 1. 큰따옴표로 둘러싸인 문자열은 + 연산과 동일
print("Life" "is" "too short") # Lifeistoo short
print("Life"+"is"+"too short") # Lifeistoo short

# 2. 문자열 띄어쓰기는 콤마로
print("Life", "is", "too short") # Life is too short

# 3. 한 줄에 결과값 출력 -> 인수 end 사용
for i in range(10):
    print(i, end=' ')