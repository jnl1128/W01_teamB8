import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split(' ')))

def splice(arr, idx):
    return arr[:idx]+arr[idx+1:len(arr)]

def diffSum(arr):
    total = 0
    for i in range(len(arr)-1):
        total += abs(arr[i+1] - arr[i])
    return total
    
def permutation(lst):
    if len(lst) == 0:
        return []
    
    if len(lst) == 1:
        return [lst]
    
    l = []

    for i in range(len(lst)):
        m = lst[i]

        for p in permutation(splice(lst, i)):
            print(p)
            l.append([m]+p)

    return l

maxV = 0

for p in permutation(A):
    maxV = max(maxV, diffSum(p))
print(maxV)