import sys
sys.setrecursionlimit(10**6)

def quick(arr, start, end):
    if(start >= end):
        return
    pivot = start
    L = start+1
    R = end
    while(L <= R):
        while(L <= end and arr[L] <= arr[pivot]): #pivot보다 큰 수를 뽑아야 하므로 반대로 함
            L+= 1
        while(R > start and arr[R] >= arr[pivot]): #pivot보다 작은 수를 뽑아야 하므로
            R-= 1
        if(L > R):
            arr[pivot], arr[R] = arr[R], arr[pivot] 
        else:
            arr[L], arr[R] = arr[R], arr[L]
    quick(arr, start, R-1)
    quick(arr, R+1, end)


a = int(input())

arr = []
for i in range(a):
    num = int(sys.stdin.readline())
    arr.append(num)

quick(arr, 0, len(arr)-1)

for i in range(len(arr)):
    print(arr[i])