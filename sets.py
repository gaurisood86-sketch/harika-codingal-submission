fruitSet={"apple" , "cherry" , "kiwi"}
print(fruitSet)
fruitSet.add("watermelon")
print("fruitSet after adding:" , fruitSet)
fruitSet.remove("cherry")
print("fruitSet after removing :" , fruitSet)


numbers={1,2,3,4,5,1,2}
print("number set:" , numbers)
numbers.add(6)
print("number set after adding 6:" , numbers)
numbers.remove(5)
print("number set after removing 5:" , numbers)


set1={1,2,3}
set2={3,4,5}

print("union:" , set1.union(set2))
print("inersection:" , set1.intersection(set2))
print("difference:" , set1.difference(set2))