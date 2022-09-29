# 09.29 12:00 구현 실패
n = int(input())
baseball = [[0] * 3 for _ in range(n)]
for i in range(n):
    baseball[i] = list(map(int, input().split()))

used = [0] * 11

available_num = []


def get_all(depth, result):
    global available_num
    if depth == 3:
        result_num = result[0] * 100 + result[1] * 10 + result[2]
        if check(result_num) is True:
            available_num.append(result_num)
        return
    for i in range(1, 10):
        if used[i] == 0:
            used[i] = 1
            get_all(depth + 1, result + [i])
            used[i] = 0


def check(result_num):
    r_1 = result_num % 10
    r_2 = result_num // 10 % 10
    r_3 = result_num // 100
    flag = True
    for b in baseball:
        b_1 = b[0] % 10
        b_2 = b[0] // 10 % 10
        b_3 = b[0] // 100
        num = [b_1, b_2, b_3]
        st = b[1]
        bl = b[2]
        
        strike_count = (r_1 == b_1) + (r_2 == b_2) + (r_3 == b_3)
        ball_count = (r_1 in num and r_1 != b_1) + (r_2 in num and r_2 != b_2) + (r_3 in num and r_3 != b_3)

        if strike_count != st or ball_count != bl:
            flag = False
            break
    
    return flag



get_all(0, [])
print(len(available_num))