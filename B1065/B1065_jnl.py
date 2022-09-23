import sys
input = sys.stdin.readline

def checkHansoo(target):
    arr = list(str(target))
    diff = int(arr[0]) - int(arr[1])
    for i in range(1, len(arr)-1):
        if int(arr[i]) - int(arr[i+1]) != diff:
            return False
    return True

N = int(input())
if N < 10:
    print(N)
else:
    cnt = 9
    for i in range(10, N+1):
        if checkHansoo(i): 
            cnt += 1
    print(cnt)






        

