def fac(n):
    result = 1
    if n > 0 :
        result = n * fac(n-1)
    return result

a = int(input())
result = fac(a)
print(result)