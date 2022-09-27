import sys
input = sys.stdin.readline

N, r, c = map(int, input().split(' '))

result = 0
def solution(r, c, n):
    global result
    if n == 0:
        return
    #0
    if 0<=r< pow(2, n-1) and 0<=c<pow(2, n-1):
        # print('#0: ', result)
        solution(r, c, n-1)

    #1
    elif 0<=r<pow(2, n-1) and pow(2, n-1)<=c<pow(2,n):
        c -= pow(2, n-1)
        result += pow(2, n-1)**2 
        # print('#1:', result)
        solution(r, c, n-1)

    #2
    elif pow(2, n-1)<=r<pow(2,n) and 0<=c<pow(2, n-1):
        r -= pow(2, n-1)
        result += pow(2, n-1)**2 * 2
        # print('#2: ', result)
        solution(r, c, n-1)
    #3
    else:
        r -= pow(2, n-1)
        c -= pow(2, n-1)
        result += pow(2, n-1)**2 * 3
        # print('#3:', result)
        solution(r, c, n-1)

solution(r, c, N)
sys.stdout.write('{}'.format(result))

