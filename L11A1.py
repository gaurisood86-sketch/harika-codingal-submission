class Animal:
    def __init__(self , name):
        self.name=name

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):

    def __init__(self , name , breed):
        super().__init__(name)
        self.breed=breed

    def bark(self):
        print(f"{self.name} is a {self.breed} and he is barking.")

dog1=Dog("oreo" , "pug")
dog1.eat()
dog1.bark()


        
    