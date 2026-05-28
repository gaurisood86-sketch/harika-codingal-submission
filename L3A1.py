with open("sample.txt" , "w") as file:
    file.write("hello this is a test file")
    file.write("python is very fun to learn")
    print("data was given sucessfully")

text="python is very fun to learn "
with open ("words.txt" , "w") as file:
    sample=text.split()
    for i in sample:
        file.write(i+"\n")
print("the data was given sucessfully")


