x , y, w, h = input().split()
x = int(x)
y = int(y)
w = int(w)
h = int(h)

arr = [0+x, 0+y, w-x, h-y]
min = arr[0]
for i in range(len(arr)):
    if(min > arr[i]):
        min = arr[i]
print(min)