a = int(input())
arr = []
arr_count = []
for i in range(a):
    arr.append([])
    arr_count.append(0)
for i in range(a):
    strr = input()
    arr[i].append(len(strr))
    arr[i].append(strr)
arr.sort()
for i in range(a-1):
    if(arr[i] == arr[i+1]):
        arr_count[i] = 1
for i in range(a):
    if(arr_count[i] == 0):
        print(arr[i][1])