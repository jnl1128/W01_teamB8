import sys
def contor(n):
    if(n == 0):
        print("-",end="")
        if(num == 0):
            print()
        return
    contor(n-1)
    for i in range(3**(n-1)):
        print(" ",end="")
    contor(n-1)
    if(n == num):
        print()
while(True):
    try:
        num = int(sys.stdin.readline())
        contor(num)
    except:
        break
    