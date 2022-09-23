def hansu(n):
    arr = []
    lest = 0
    while (n != 0):
        lest = n % 10
        arr.append(lest) 
        n = n // 10
    diff = []
    for i in range(len(arr)-1):
        minus = arr[i] - arr[i+1]
        diff.append(minus)
    count = 0
    for i in range(len(diff)):
        if(diff[0] != diff[i]):
            count += 1
    return count

#메인함수
a = int(input())
count = 0

for i in range(1, a+1):
    if(hansu(i) == 0):
        count += 1
print(count)