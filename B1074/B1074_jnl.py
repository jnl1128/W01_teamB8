N, r, c = map(int, input().split(' '))
boxNum = 0
arr =[]
def whichBox(a, n):
    global arr, boxNum, r, c
    if n < 1:
        arr = a
        return 
    if (r >=0 and c>=0) and (r<=pow(2, n-1)-1 and c<=pow(2, n-1)-1):
        boxNum += 0 * (pow(2, n-1)**2)
        whichBox([[0,0], [pow(2, n-1)-1, pow(2, n-1)-1]], n-1)
    elif (r>=0 and c>=pow(2,n-1)) and (r<=pow(2, n-1)-1 and c<=pow(2, n)-1):
        boxNum += 1 * (pow(2, n-1)**2)
        c -= pow(2,n-1)
        whichBox([[0, pow(2, n-1)], [pow(2, n-1)-1, pow(2, n)-1]], n-1)
    elif (r>=pow(2, n-1) and c>=0) and (r<=pow(2, n)-1 and c <=pow(2, n-1)-1):
        boxNum += 2 * (pow(2, n-1)**2)
        r -= pow(2, n-1)
        whichBox([[pow(2,  n-1),0], [pow(2, n)-1, pow(2, n-1)-1]], n-1)
    else:
        boxNum += 3 * (pow(2, n-1)**2)
        r -= pow(2,n-1)
        c -= pow(2, n-1)
        whichBox([[pow(2,n-1), pow(2, n-1)], [pow(2, n)-1, pow(2, n)-1]], n-1)

if N == 1:
    print((r+1)*r+c)
else:  
    whichBox(arr, N)
    print(boxNum)
