import sys
input = sys.stdin.readline

H, W = map(int, input().split(' '))
T = int(input())
arrH = [0,H]
arrW = [0,W]
for _ in range(T):
    axis, idx = map(int, input().split(' '))
    if axis == 0:
        arrW.append(idx)
        arrW.sort()
    else:
        arrH.append(idx)
        arrH.sort()
maxW = max([arrW[i+1]-arrW[i] for i in range(len(arrW)-1)])
maxH = max([arrH[i+1]-arrH[i] for i in range(len(arrH)-1)])
# print([arrW[i+1]-arrW[i] for i in range(len(arrW)-1)], [arrH[i+1]-arrH[i] for i in range(len(arrH)-1)])
print(maxH*maxW)


