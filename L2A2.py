with open ("sample.txt" , "r") as file:
    print("reading part of the line")
    print(file.read(10))

with open ("sample.txt" , "r") as file:
    print("reading one single line")
    print(file.readline())

with open ("sample.txt" , "r") as file:
    print("looping through file lines")
    for line in file:
        print(line.strip())
