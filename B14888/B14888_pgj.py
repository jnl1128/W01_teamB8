import sys



def calculater(arr_num, cal_arr):
    global max_num, min_num
    sum = arr_num[0] #첫 값은 넣어줌
    cnt = 1  #
    while(num > cnt):
        if(cal_arr[cnt-1] == '0'):
            sum += arr_num[cnt]
        elif(cal_arr[cnt-1] == "1"):
            sum -= arr_num[cnt]
        elif(cal_arr[cnt-1] == "2"):
            sum *= arr_num[cnt]
        else:
            if (sum//arr_num[cnt] < 0):
                sum = -(-sum//arr_num[cnt])
            else:
                sum = sum//arr_num[cnt]
        cnt+=1
    if(sum > max_num):
        max_num = sum
    if(sum < min_num):
        min_num = sum

def permutation(arr, r):
    global chosen, used

    # 선택리스트에 순열의 원소를 저장하다가 갯수가 r개가 되면 출력 후 함수를 종료한다.
    if len(chosen) == r:
        calculater(arr_num, chosen)
        return

    # 반복문을 돌면서
    for i in range(len(arr)):
        # 아직 사용하지 않았다면
        if not used[i]:
            # 선택리스트에 저장하고 방문체크한다.
            chosen.append(arr[i])
            used[i] = 1
            # 다시 generate 함수를 반복한다.
            permutation(arr, r)
            # 하나의 순열이 만들어지면 다시 uncheck한다.
            used[i] = 0
            chosen.pop()
    


num = int(sys.stdin.readline())
arr_num = list(map(int, sys.stdin.readline().split()))
arr_cal_num = list(map(int, sys.stdin.readline().split()))

arr_cal = []
for i in range(4):
    if(arr_cal_num[i] == 0):
        pass
    for j in range(arr_cal_num[i]):
        if(i == 0):
            arr_cal.append('0')
        elif(i == 1):
            arr_cal.append('1')
        elif(i == 2):
            arr_cal.append('2')
        else:
            arr_cal.append('3')

chosen = []
used = [0 for _ in range(num-1)]
max_num = -1e9 #글로벌
min_num = 1e9 #글로벌

permutation(arr_cal, num-1)


sys.stdout.write(f'{max_num}\n{min_num}')
