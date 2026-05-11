fruits=("apple" , "watermelon" , "strawberry" , "blueberry","kiwi" )
print("fruits tuple:" , fruits)

print ("first fruit:" , fruits[0])
print("second fruit:" , fruits[1])

print("last fruit:" , fruits[-1])


print("first two fruits:" , fruits[0:2])

for i in fruits:
    print(i)

print("apple count:" , fruits.count("apple"))
print("index of kiwi:" , fruits.index("kiwi"))