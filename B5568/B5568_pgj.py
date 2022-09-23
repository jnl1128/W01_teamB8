import sys
import itertools


arr = []
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

for i in range(n):
    arr.append(int(input()))
dict_num = set()
for i in list(itertools.permutations(arr, k)):
    dict_num.add(''.join(list(map(str, i))))
print(len(dict_num))
