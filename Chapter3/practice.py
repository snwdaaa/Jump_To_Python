# 연습문제

# while문

# 1. 별찍기
i = 0
while True:
    i += 1
    if(i > 5): break
    print("*" * i)


# for문

# 1. 학생 성적 리스트. for문으로 학생 평균 점수 구하기
A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for i in A:
    total += i
average = total / len(A)
print(average)