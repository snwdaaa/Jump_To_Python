# 연습 문제

# 함수

# 1. 정수 n을 입력받아서 n 이하까지의 피보나치 수열을 출력하는 함수
def fibo(n):
    if(n == 0):
        return 0
    if (n == 1):
        return 1

    return fibo(n-2) + fibo(n-1)

num = input("n을 입력하세요: ")
for i in range(0, int(num)):
    print(fibo(i))

# 파일 읽고 쓰기

# 1. 10줄로 이루어진 sample.txt 파일의 모든 숫자값을 읽어 총합과 평균값을 구한 후, 평균값을 result.txt에 저장하는 프로그램
f = open("C:/Users/kkj48/Desktop/Programming/Jump_To_Python/Chapter4/sample.txt", 'r')
lines = f.readlines()
f.close()

total = 0
for line in lines:
    score = int(line)
    total += score

average = total / 10

f = open("C:/Users/kkj48/Desktop/Programming/Jump_To_Python/Chapter4/result.txt", 'w')
f.write(str(average))
f.close()