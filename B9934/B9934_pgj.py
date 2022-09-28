import sys

def binary_perfact_tree(start_p, end_p, n):
    if start_p == end_p:
        tree[n].append(arr[start_p])
        return
    mid = (start_p + end_p)//2
    tree[n].append(arr[mid])
    binary_perfact_tree(start_p,mid-1,n+1)
    binary_perfact_tree(mid+1,end_p,n+1) 




num = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split())) 
tree = [[] for _ in range(num)] #트리를 깊이 단위로 저장할 리스트
start = 0
end = len(arr)-1
binary_perfact_tree(start, end, 0)
for i in range(len(tree)):
    for j in range(len(tree[i])):
        print(tree[i][j],end=" ")
    print()
