n=int(input())
t=n
def factorial(n):
    global t
    t=t*(n - 1)
    n = n - 1
    if n>1:
        factorial(n)
    return t


print(factorial(n))