import sys

count = [0] * 10001	# 10000 이하의 자연수

for i in range(int(sys.stdin.readline())): #입력받은 수
    count[int(sys.stdin.readline())] += 1 
    #입력받은 수 index에 카운트

for i in range(len(count)):
    while (count[i] > 0):
        print(i)
        count[i] -=1