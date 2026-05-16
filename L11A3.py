class Robot:
    def __init__(self , name , model):
        self.name=name
        self.model=model

    def introduce(self):
        print(f"Hello my name is {self.name} , i am model {self.model}")


robot1=Robot("Tom" , "10.0x")
robot2=Robot("Jerry" , "20.0x")

robot1.introduce()
robot2.introduce()