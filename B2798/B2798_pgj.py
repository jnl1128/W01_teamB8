a, b = map(int, input().split())

arr = list(map(int, input().split()))

sum_abc = arr[0]+ arr[0] + arr[0]
result = 0
cnt = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            sum_abc = arr[i]+ arr[j] + arr[k]
            if(sum_abc <= b):
                cnt+= 1
                if(cnt == 1):
                    result = sum_abc
                elif(b - result > b - sum_abc):
                    result = sum_abc

print(result)