#별 #
import sys, math
input =  sys.stdin.readline

N = int(input())
#2^N~1
#총 가로 길이: 8, depth = gap = 0 (<-2의 승수)
#총 가로 길이: 7, depth = gap = 1
#총 가로 길이: 6, depeth = gap = 2
#총 가로 길이: 5, depeth = gap = 3
#총 가로 길이: 4, depeth = gap = 0 (<-2의 승수)
#총 가로 길이: 3, depeth = gap = 1 
#총 가로 길이: 2, depeth = gap = 0 (<-2의 승수)
#총 가로 길이: 1, depeth = gap = 0 (<-2의 승수)

def solution(depth, flag,closest):
    if depth== 1:
        print('*')
        return

    if flag:
        print('*'*depth)
        solution(depth-1, False,depth)
    else:
        gap = closest - depth #1이상임. 0인 경우는 flag = 0 이므로 여기로 분기 안됨
        i = 0
        if depth % 2 == 0:
            while i < depth-gap:
                print('*'*gap,end='')
                print(' '*gap,end='')
                i += gap*2
            print('*'*gap)
        else:
            while i <depth-1:
                print('*', end ='')
                print(' '*gap, end='')
                i += 1+gap
            print('*')
        # if depth-1 == 4:
        #     print(math.log2(depth-1), math.log2(closest)-1, closest)
        if math.log2(depth-1) == math.log2(closest)-1:
            print('!')
            solution(depth-1, True, depth-1)
        else:
            solution(depth-1, False, closest)

if N == 0:
    print('*')
elif N == 1:
    print('**\n*')
else:
    solution(pow(2, N),True, pow(2, N))
