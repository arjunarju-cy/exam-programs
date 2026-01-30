#recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter n: "))

print("Fibonacci number:", fibonacci(n))

#iteration
n = int(input("Enter n: "))

a, b = 0, 1

if n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    for _ in range(2, n + 1):
        a, b = b, a + b
    print("Fibonacci number:", b)

