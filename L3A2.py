import os
try:
    with open ("newfile.txt" , "x") as file:
        file.write("this is a newly created file")
    print("the was created sucessfully")
except FileExistsError:
    print("this file already exists")

filename="sample.txt"
if os.path.exists(filename):
    print("this file exists")
else:
    print("this file does not exist")



filename="data.txt"
if not os.path.exists(filename):
    with open ("data.txt" , "w") as file:
     file.write("this is a newly created file")
    print("the file has been created")
else:
    print("this file alreadly exists")

filename="sample.txt"
if os.path.exists(filename):
    os.remove(filename)
    print(f"the {filename} has been deleted sucessfully")
else:
    print(f"file {filename} does not exist")


folder_name="testfolder"
if os.path.exists(folder_name):
    os.rmdir(folder_name)
    print(f"the {folder_name} has been deleted sucessfully")
else:
    print(f" this folder {folder_name} does not exist")                                             