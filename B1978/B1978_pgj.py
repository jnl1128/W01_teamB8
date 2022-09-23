a = int(input())
arr = []
for i in range(a):
    arr.append(0)

arr = input().split()
arr = list(map(int, arr))

result_count = 0
for  i in range(len(arr)):
    
    count = 0
    for j in range(1, arr[i]+1):

        result = arr[i] % j
        if(result == 0):
            count+=1

    if(count == 2):
        result_count+=1


print(result_count)