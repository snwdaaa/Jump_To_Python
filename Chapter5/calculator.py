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