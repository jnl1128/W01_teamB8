import sys

p_num = [True for _ in range(10001)]
p_num[0] = False
p_num[1] = False

for i in range(2, 10001):
    if p_num[i] is True:
        for j in range(i*2, 10001, i):
            p_num[j] = False

tc = int(sys.stdin.readline().rstrip())
for _ in range(tc):
    n = int(sys.stdin.readline())
    for i in range(n//2, 1, -1):
        if p_num[i] and p_num[n-i]:
            sys.stdout.write(f'{i} {n-i}\n')
            break