arr = []
for i in range(9):
    a = int(input())
    arr.append(a)
temp1, temp2 = 0, 0
for i in range(9):
    for j in range(i+1, 9):
        if(sum(arr) - (arr[i] + arr[j]) == 100):
            temp1 = arr[i]
            temp2 = arr[j]
            break
        
arr.remove(temp1)
arr.remove(temp2)

arr.sort()

for i in range(len(arr)):
    print(arr[i])
