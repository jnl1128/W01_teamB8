import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
cards = []
visited = [False for _ in range(n)]
for _ in range(n):
    cards.append(input().rstrip())

# 만든 수열을 저장할 집합
result_set = set()

def solution(depth, string):
    # 가장 끝(바닥)까지 내려갔을 경우
    if depth == k:
        # 집합에 추가하기(문자열로 하는 이유: set의 원소로는 리스트가 들어갈 수 없음)
        result_set.add(string)
        # 끝까지 내려갔으니까 이 수열은 끝났음
        return
    for i in range(len(cards)):
        # 아직 사용하지 않은 카드인지
        if visited[i] == False:
            # 이번에 사용할거고
            visited[i] = True
            # 한층 더 깊이 내려갔다 오겠음
            solution(depth+1,string+cards[i])
            # 마지막으로 사용하기로 한거 무효화
            visited[i] = False

solution(0, '')
print(len(result_set))