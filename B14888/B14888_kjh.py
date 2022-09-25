import sys

n = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))

min_result = 1000000001
max_result = -1000000001
def solution(depth, sum):
    global num_list
    global min_result
    global max_result

    if depth == n:
        min_result = min(min_result, sum)
        max_result = max(max_result, sum)
        return

    for i in range(4):
        if operator[i] > 0:
            operator[i] -= 1
            next_sum = 0
            if i == 0:
                next_sum = sum + num_list[depth]
            elif i == 1:
                next_sum = sum - num_list[depth]
            elif i == 2:
                next_sum = sum * num_list[depth]
            else:
                if sum < 0:
                    next_sum = -(-sum // num_list[depth])
                else:
                    next_sum = sum // num_list[depth]
            solution(depth+1, next_sum)
            operator[i] += 1

solution(1, num_list[0])
sys.stdout.write(f'{max_result}\n{min_result}')