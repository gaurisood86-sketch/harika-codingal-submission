friends=["paridhi" , "radhika" , "ritvi"]
print("friends good at math :" , [0] )
print("friends good at english :" , [1])
print("friends good at science :" , [2])

friends [2]="ananya"
print("/n creating a list after changing a value :" , friends)

count=1
for i in friends:
    print(f"friend number {count} = {i}")
count=count+1
print("/n creating a loop with list")

friends.append("harika")
print("creating a list using append method")
print(friends)




harika = {
    "name" : "harika trehan",
    "age" : 12,
    "skill" : "art",
}

harika["skill"]= "table tennis"
print("\n printing with changes :" , harika)

harika["bday"] = "19/01/2014"
print("\n printing the new value:" , harika)

