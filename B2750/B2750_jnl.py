import sys
input = sys.stdin.readline

N = int(input())

negArr = [0] * 1000001
posArr = [0] * 1000001

for _ in range(N):
    num = int(input())
    if num < 0:
        negArr[-1*num] = 1
    else:
        posArr[num] = 1

result = [] 
negArr.reverse()

for idx, num in enumerate(negArr):
    if num != 0:
        result.append(-(1000000-idx))
for idx, num in enumerate(posArr):
    if num != 0:
        result.append(idx)


for el in result:
    print(el)