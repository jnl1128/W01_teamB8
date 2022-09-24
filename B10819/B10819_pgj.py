import sys
import itertools
sys.setrecursionlimit(100001)

a = int(sys.stdin.readline())
arr = []
arr = list(map(int, sys.stdin.readline().split()))


per_arr = []
for i in list(itertools.permutations(arr, len(arr))):
    per_arr.append(list(map(int, i)))

result = 0
for i in range(len(per_arr)):
    sum = 0
    for j in range(0, a-1):
        sum += abs(per_arr[i][j]-per_arr[i][j+1])
    if(sum > result):
        result = sum
print(result)