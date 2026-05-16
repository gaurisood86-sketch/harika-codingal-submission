class Addition:
    def __init__(self , num1 , num2 , num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3

    def sum(self):
        total=self.num1+self.num2+self.num3
        print(f"the total of the numbers is {total}")
number=Addition(10 , 20 , 30)
number.sum()