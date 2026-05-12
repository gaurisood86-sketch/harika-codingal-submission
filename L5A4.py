def fibonacci(n):
    a, b = 0, 1
    series = []
    
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    
    return series


num_terms = int(input("Enter the number of terms: "))

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Fibonacci series: {fibonacci(num_terms)}")
