def num_check(num):
    pre = int(num[0])-int(num[1])
    for i in range(1, len(num)-1):
        if pre != int(num[i])-int(num[i+1]):
            return 0
    return 1

n = int(input())
if n < 100:
    print(n)
else:
    count = 99
    for num in range(100, n+1):
        count += num_check(str(num))
    print(count)