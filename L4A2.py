
for i in range(1, 11):
    print(f"23 x {i} = {23 * i}")


total_sum = 0
num = 1
while num <= 10:
    total_sum += num
    num += 1
print(f"The sum of the first ten natural numbers is {total_sum}")



num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")