
num = int(input("Enter a number: "))
num_str = str(num)
num_digits = len(num_str)
armstrong_sum = 0
x = num
while x > 0:
    digit = x % 10            
    armstrong_sum += digit ** num_digits  
    x //= 10                

if num == armstrong_sum:
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not an armstrong number")
