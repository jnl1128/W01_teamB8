#완전 이진 트리
import sys
input = sys.stdin.readline

K = int(input())
#인풋으로 받는 리스트가 전위순회한 결과
routes = list(input().rstrip().split(' '))
#i번째 원소 = i번째 depth에 있는 수(왼->오 순)
kArr = ['' for _ in range(K+1)]

def solution(depth, arr):
    if depth == 1:
        kArr[depth] += arr[0]+' '
        return
    
    midIdx = len(arr)//2
    kArr[depth] += arr[midIdx]+' '
    solution(depth-1, arr[:midIdx])
    solution(depth-1, arr[midIdx+1:])

solution(K,routes)

kArr = kArr[::-1][:-1]
for string in kArr:
    if len(string)>1:
        tmp = string.rstrip().split(' ')
    else:
        tmp = [string]
    for idx, elem in enumerate(tmp):
        if idx == len(tmp)-1:
            print(elem)
        else:
            print(elem, end =' ')
    