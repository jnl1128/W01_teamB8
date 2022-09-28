#이진 검색 트리
import sys
input = sys.stdin.readline
print = sys.stdout.write

# 전위순회
pre_nodes = []
while True:
    try:
        node = int(input().rstrip())
    except:
        break
    pre_nodes.append(node)

N = len(pre_nodes) #9

def solution(start, end):
    if end-start == 2:
        print(pre_nodes[start])
        return
    if start < end:
        top = pre_nodes[start] #(0)50 #(1)30 #(2)24
        m = 0
        for idx, node in enumerate(pre_nodes[start:end]):
            if node > top:
                m = idx
                break
        # m = 6 # m = 2 # m=1
        solution(start+1, start+m) # sol(1, 6) #sol(2, 4)
        solution(start+m, end) # sol(6, 9)
        print(top) #50

solution(0, N)


