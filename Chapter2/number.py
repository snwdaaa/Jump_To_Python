# 02-1. 숫자형

# 정수형
num_int = 123
num_int = -178
num_int = 0
print(num_int)

# 실수형
num_float = 1.2
num_float = -3.45
print(num_float)

# 실수형-지수 표현 방식(E, e)
num_exp = 4.24E10
num_exp = 4.24e-10
print(num_exp)

# 8진수와 16진수
num_octal = 0o117 # 8진수를 선언하려면 접두사 '0o' or '0O' 붙이기 (0 'o'ctal)
num_hex1 = 0x8ff # 16진수를 선언하려면 접두사 '0x' 붙이기 (0 he'x'adecimal)
num_hex2 = 0xABC

# 복소수
num_comp = 1+2j # 고등학교 때 쓰던 i 대신 j or J 사용
# 복소수 - 활용
num_comp.real # 복소수.real : 실수부 리턴
num_comp.imag # 복소수.imag : 허수부 리턴
num_comp.conjugate # 복소수.conjugate : 켤레복소수 리턴
num_comp.abs # 복소수.abs : 복소수의 절댓값 리턴

# 제곱 연산자 '**'
num_exponential = 3 ** 4 # 3^4

# 나머지 연산자
7 % 3 # 1

# 나눗셈 후 몫의 소수점 아래자리 버리는 연산자
7 // 4 # 1.75 -> 1 (.75 버림)