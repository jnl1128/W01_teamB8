def hanoi(n, start, end, aux): 
#n : 반복할 횟수, start: 원반의 시작점, end, 원반의 도착점, aux : 원반의 경유지
    if(n == 1):
        print(start, end)
        return
    hanoi(n-1, start, aux, end)
    hanoi(1, start,end,aux)
    hanoi(n-1, aux, end, start)

n = int(input())
print(2**n-1)
if(n <= 20):
    hanoi(n,1,3,2)
