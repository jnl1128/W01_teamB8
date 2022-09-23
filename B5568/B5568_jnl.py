from itertools import permutations

strArr = []
n = int(input())
k = int(input())
for _ in range(n):
    strArr.append(input())

strSet = set()
for tup in list(permutations(strArr, k)):
    strSet.add(''.join(tup))
print(len(strSet))
