import sys

tc = int(sys.stdin.readline().rstrip())

count_array = [0 for _ in range(10001)]

for _ in range(tc):
    num = int(sys.stdin.readline().rstrip())
    count_array[num] += 1

for i in range(len(count_array)):
    for _ in range(count_array[i]):
        sys.stdout.write(f'{i}\n')
