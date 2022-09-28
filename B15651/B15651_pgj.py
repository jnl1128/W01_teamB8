import sys

def dfs(arr, n):
    result_arr = []
    if n > len(arr):
        return result_arr

    if n == 1:
        for i in arr:
            result_arr.append([i])
    elif n > 1:
        for i in range(len(arr)):
            for j in dfs(arr, n-1):
                result_arr.append([arr[i]]+j)
    
    return result_arr

num, repeat_num = map(int, sys.stdin.readline().strip().split())

arr_num = list(range(1, num+1))

result_arr = dfs(arr_num, repeat_num)

for elem in result_arr:
    print(*elem, sep=' ')