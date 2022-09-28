from copy import deepcopy
import sys

def dfs(arr, n):
    result_arr = []


    if n == 1:
        for i in arr:
            result_arr.append([i])
    elif n > 1:
        ans = deepcopy(arr)
        for i in range(len(arr)):
            ans.pop(0)
            for j in dfs(ans, n-1):
                result_arr.append([arr[i]]+j)
    return result_arr

num, repeat_num = map(int, sys.stdin.readline().strip().split())

arr_num = list(map(int,sys.stdin.readline().strip().split()))
arr_num.sort()
result_arr = dfs(arr_num, repeat_num)

for elem in result_arr:
    print(*elem, sep=' ')