class Calc():
    def __init__(self,height,weight):
        self.__height = height
        self.__weight = weight

    def set_height(self,height):
        self.__height = height
    
    def get_height(self):
        return self.__height

    def set_weight(self,weight):
        self.__weight = weight
    
    def get_weight(self):
        return self.__weight
    
    def BmiCalc(self):
        bmi = self.__weight / (self.__height * self.__height)
        return bmi

    
height = input("身長を入力してください >")
weight = input("体重を入力してください >")
calc = Calc(height,weight)
bmi = calc.BmiCalc()
print("あなたのBIMは{}です".format(round(bmi,1)))