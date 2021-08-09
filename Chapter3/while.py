# while문

treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if(treeHit == 10):
        print("나무 넘어갑니다")

'''
# while문 예제
# 여러 가지 선택지 중 하나를 선택해서 입력받는다
prompt = """
    1. Add
    2. Del
    3. List
    4. Quit

    Enter number: """

number = 0

while (number != 4):
    print(prompt)
    number = int(input()) # 입력 받기
'''

# while문 강제로 빠져나가기 -> break문
# 커피 자판기 예제
coffee = 10
money = 300

while (money):
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print("남은 커피의 양은 %d개 입니다." % coffee)

    if(not coffee): # coffee가 0(False)일 때 not coffee는 True이므로 if문 실행
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break # while문 탈출

"""
# 커피 자판기 예제 2
coffee = 10
while True:
    money = int(input("돈을 넣어주세요: "))

    if(money == 300):
        print("커피를 줍니다.")
        coffee -= 1
    elif (money > 300):
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee -= 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    
    if (not coffee):
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break # while문 탈출
"""

# continue문
a = 0
while(a < 10):
    a += 1
    
    if(a % 2 == 0): continue # 짝수면 continue -> 건너 뛰고 while문의 처음으로 가서 다음 작업을 수행한다.
    print(a)
