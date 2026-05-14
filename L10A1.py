class Apple:
    def __init__(self , product):
        self.product=product
        print("this object has been created ")

    def details (self):
        print(f"this is an apple {self.product}")

    def __del__ (self):
        print("this object has been deleted")

macbook=Apple("macbook pro")
macbook.details()


class Animal:
    def __init__(self , name):
        self.name=name
        print(f"this is {self.name} ")

    def sound(self):
        print(f"{self.name} is making a sound")

    def walking(self):
        print(f"{self.name} is walking")

    def __del__(self):
        print(f"{self.name} is deleted")

dog=Animal("oreo")
dog.sound()
dog.walking()

cat=Animal("milkshake")
cat.sound()
cat.walking()

del dog
del cat

    