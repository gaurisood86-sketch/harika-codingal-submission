with open ("sample.txt" , "r") as file:
    lines=file.readlines()
    print(lines)

with open ("sample.txt" , "r") as file:
    print(file.read(10))

with open ("sample.txt" , "r") as file:
    line=file.readline()
    print(line)

with open ("sample.txt","r") as file:
    print(file.readline(4))

with open ("sample.txt" , "r") as file:
    for line in file.readlines():
        print(line.strip()) 

























