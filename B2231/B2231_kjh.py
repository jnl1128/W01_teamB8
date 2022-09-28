n = int(input())
flag = True
if n % 2 == 1:
    print('0')
else:
    for i in range(n+1):
        tmp = i
        sum = i
        while tmp > 0:
            sum += tmp % 10
            tmp //= 10
        if sum == n:
            print(i)
            break
