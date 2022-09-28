#칸토어 집합 #언더바가 아니라 #-
import sys
input = sys.stdin.readline

def solution(depth, line):
    if depth == 0:
        print(line, end ='')
        return
    nl = pow(3, depth)//3
    solution(depth-1, line[:nl]) 
    print(' '*nl, end ='')
    solution(depth-1, line[nl*2:])



while True:
    try:
        n = int(input().rstrip())
    except:
        break
    solution(int(n), '-'*pow(3, int(n)))
    print('')
