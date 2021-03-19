def fibonacci(f):
    if f == 0 or f == 1:
        return f
    if f == 2:
        return 1
    else:
        return fibonacci(f - 1) + fibonacci(f - 2)

def tribonacci(n):
    if n == 0 or n == 1:
        return n
    elif n == 2:
        return 1
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
print(tribonacci(25))