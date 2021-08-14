# 연습 문제

# 클래스
# 1. Calculator 클래스 만들기

# sum, avg 함수
# sum 함수는 입력으로 리스트를 받는다.

class Calculator:
    def __init__(self, inputList):
        self.numList = inputList

    def sum(self):
        self.sum = 0
        
        for i in range(0, len(self.numList)):
            self.sum += self.numList[i]
        
        print(self.sum)

    def avg(self):
        self.avg = self.sum / len(self.numList)

        print(self.avg)

cal1 = Calculator([1,2,3,4,5])
cal1.sum()
cal1.avg()

cal2 = Calculator([6,7,8,9,10])
cal2.sum()
cal2.avg()


# 모듈
# 1. 위의 Calculator 클래스를 calculator.py로 만든 후, 모듈 형식으로 사용
from calculator import Calculator

calc1 = Calculator([1,2,3,4,5])
calc1.sum()