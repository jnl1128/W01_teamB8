c = int(input())
for _ in range(c):
    n, *l = map(int, input().split())
    avg = sum(l)/n
    print(f'{(sum(1 for i in l if i > avg) / n) * 100:.3f}%')
