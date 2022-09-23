tc = int(input())
for _ in range(tc):
    n, s = input().split()
    print(*[i*int(n) for i in s], sep="")