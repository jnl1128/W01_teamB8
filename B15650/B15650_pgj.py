def dfs(arr, n):
    result_arr = []
    if n > len(arr):
        return result_arr

    if n == 1:
        for i in arr:
            result_arr.append([i])
    elif n > 1:
        for i in range(len(arr) -n + 1):
            for j in dfs(arr[i+1:], n-1):
                result_arr.append([arr[i]]+j)
    
    return result_arr

num, repeat_num = map(int, input().split())

arr_num = []
for i in range(1,num+1):
    arr_num.append(i)


result_arr = dfs(arr_num, repeat_num)
for i in range(len(result_arr)):
    for j in range(repeat_num):
        print(result_arr[i][j], end=" ")
    print()