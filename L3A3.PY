text="HELLO MY NAME IS HARIKA.I AM IN GRADE 8. I AM 12 YEARS OLD."

with open ("sample.txt" , "w") as file:
    sample=text.split()
    for i in sample:
        file.write(i+"\n")
print("the data was given sucessfully")

import os
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