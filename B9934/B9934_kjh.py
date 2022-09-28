K = int(input())
visit = list(map(int, input().split()))

tree = [[] for _ in range(K)]

def solution(depth, visit):
    if depth == 0:
        return
    # 중위 순회(왼-루트-오)로 입력된
    # 깊이가 depth인 완전이진트리의 정점의 위치는
    # 왼쪽 마지막 자식의 갯수로 결정할 수 있다.
    x = (2**(depth-1)) - ((2**depth - 1) - len(visit))
    left = x if (2**(depth-1)) // 2 > x else (2**(depth-1))//2
    root_idx = (2**(depth-1) - 1) // 2 + left

    tree[K-depth].append(visit[root_idx])

    solution(depth-1, visit[:root_idx])
    solution(depth-1, visit[root_idx+1:])

solution(K, visit)

for i in range(len(tree)):
    print(*tree[i], sep=" ")