import sys
import itertools
def perm(arr, n):
    result = []
    if(n > len(arr)):
        return result
    if(n == 1): #순열에서 고르는 값이 1일 경우 = 배열 그 자체인 경우
        for i in arr:
            result.append([i])
    elif (n > 1):
        for i in range(len(arr)):
            copy_arr = [i for i in arr] # arr을 복사
            copy_arr.remove(arr[i])
            for p in perm(copy_arr, n-1):
                result.append([arr[i]]+p)
    return result


arr = []
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

for i in range(n):
    arr.append(int(input()))
dict_num = perm(arr, k)

result_arr = []
for i in range(len(dict_num)):
    str_arr = ""
    for j in range(len(dict_num[i])):
        str_arr += str(dict_num[i][j])
    if str_arr not in result_arr:
        result_arr.append(str_arr)

print(len(result_arr))

# dict_num = set()
# for i in list(itertools.permutations(arr, k)):
#     dict_num.add(''.join(list(map(str, i))))
# print(len(dict_num))
# itertools 라이브러리를 이용하면 더 쉽게 풀 수 잇다

