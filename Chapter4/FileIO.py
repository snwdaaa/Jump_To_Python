# 파일 읽고 쓰기

# 1. 파일 생성하기
# 파이썬 내장함수 open
# 파일객체 = open(파일경로, 열기모드)
# 열기모드 -> w(쓰기), r(읽기), a(추가)
# 파일 경로는 "/"만. \ 안 됨
f = open("C:/Users/kkj48/Desktop/Programming/Jump_To_Python/Chapter4/NewFile.txt", 'w')
f.close()



# 2. 쓰기 모드로 열어 출력값 적기
# 파일.write("문자열") : 파일에 인수로 주어진 문자열을 입력한다.
f = open("C:/Users/kkj48/Desktop/Programming/Jump_To_Python/Chapter4/writedata.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()



# 3. 외부 파일 읽는 여러가지 방법

# a. readline() 함수 : 한 줄씩 읽는다.
# 반복문에서 사용하면 다음 줄도 읽을 수 있다.
# 더 이상 읽을 줄이 없으면 None 리턴

# 한 줄 읽기
f = open("C:/Users/kkj48/Desktop/Programming/Jump_To_Python/Chapter4/writedata.txt", 'r') # read
line = f.readline()
print(line)
f.close()

# 모든 라인 읽기
f = open("C:/Users/kkj48/Desktop/Programming/Jump_To_Python/Chapter4/writedata.txt", 'r') # read
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# b. readlines() 함수 : 파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 리스트 리턴
f = open("C:/Users/kkj48/Desktop/Programming/Jump_To_Python/Chapter4/writedata.txt", 'r') # read
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# c. read() 함수 : 파일 내용 전체를 문자열로 리턴
f = open("C:/Users/kkj48/Desktop/Programming/Jump_To_Python/Chapter4/writedata.txt", 'r') # read
data = f.read() # 전체 내용을 한 문자열로 받아옴
print(data)
f.close()



# 4. 기존 파일에 새로운 내용 추가하기
# => 'a'(추가 모드) 사용
f = open("C:/Users/kkj48/Desktop/Programming/Jump_To_Python/Chapter4/writedata.txt", 'a') # append
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()


# 5. with문
# with 블록을 벗어나는 순간 열린 파일 객체가 자동으로 close됨
with open("C:/Users/kkj48/Desktop/Programming/Jump_To_Python/Chapter4/writedata.txt", 'r') as f: # f로서 파일 객체를 가져옴
    data = f.read()