def f(n):
    if n == 0 or n == 1: return 1
    elif n<0: return EOFError
    else: return f(n-1) + f(n-2)

print(f(10))