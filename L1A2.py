with open("sample.txt" , "w") as file:
    file.write("hello welcome to file management")

with open("sample.txt", "r") as file:
    date=file.read()
    print(date)

with open ("sample.txt","a") as file:
    file.write("\nyou are reading the file")
with open ("sample.txt","r") as file:
    data=file.read()
    print(data)