class Students:
    def __init__(self , name , age , grade):
        self.name=name
        self.age=age
        self.grade=grade
        print(f" the record has been created for {self.name} ")

    def showDetails(self):
        print(f"name:{self.name}")
        print(f"age: {self.age}")
        print(f"grade: {self.grade}")

    def updatedGrade(self ,new_grade):
        self.grade=new_grade
        print(f"student {self.name} grade has been updated to {self.grade}")

    def __delete__(self):
        print(f"student record for {self.name} has been deleted")

print("Welcome to student manegment system")
student1=Students("gauri" , "13" , "9th")
student1.showDetails()

student2=Students("harika" , "12" , "7th")
student2.showDetails()
student2.updatedGrade("8th")
del student2 