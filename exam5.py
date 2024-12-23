def sin_series(x,tol):
    series = 0
    i = 1
    flag = 1
    term = 1
    while tol <= term :
        term = x**i/factorial(i)
        if flag % 2 == 0:
            series -= term
        else:
            series += term
        i += 2
        flag = flag +1
    return round(series,6)
def factorial(n):
    if n < 2:
        return 1
    fact = 1
    for i in range(n,1,-1):
        fact *= i
    return fact
    