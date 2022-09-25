import itertools
import sys

num = int(sys.stdin.readline())
arr_num = list(map(int, sys.stdin.readline().split()))
arr_cal_num = list(map(int, sys.stdin.readline().split()))

arr_cal = []
arr_cal_cnt = 0
for i in range(4):
    if(arr_cal_num[i] == 0):
        pass
    for j in range(arr_cal_num[i]):
        if(i == 0):
            arr_cal.append('+')
        elif(i == 1):
            arr_cal.append('-')
        elif(i == 2):
            arr_cal.append('*')
        else:
            arr_cal.append('/')
        arr_cal_cnt += 1


arr_case = list(set(itertools.permutations(arr_cal, arr_cal_cnt)))
# 연산자가 발생할 수 있는 모든 경우의 수

arr_result = [] #연산자와 숫자가 모두 포함된 함수
for j in range(len(arr_case)):
    cnt_cal = 0
    cnt_num = 0
    arr = []
    for i in range(num+sum(arr_cal_num)):
        if(i % 2 == 0):
            arr.append(arr_num[cnt_num])
            cnt_num+= 1
        else:
            arr.append(arr_case[j][cnt_cal])
            cnt_cal+= 1
    arr_result.append(arr)


max_num = -1e9
min_num = 1e9
for i in range(len(arr_result)):
    sum = arr_result[i][0]
    for j in range(1, num+arr_cal_cnt, 2):
        if(arr_result[i][j] == "+"):
            sum += arr_result[i][j+1]
        elif(arr_result[i][j] == "-"):
            sum -= arr_result[i][j+1]
        elif(arr_result[i][j] == "*"):
            sum *= arr_result[i][j+1]
        else:
            if (sum//arr_result[i][j+1] < 0):
                sum = -(-sum//arr_result[i][j+1])
            else:
                sum = sum//arr_result[i][j+1]

    if(sum > max_num):
        max_num = sum
    if(sum < min_num):
        min_num = sum
print(max_num)
print(min_num)