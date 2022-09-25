# 다른 사람 풀이 참고함

# a, b, c 기둥이 있다고 하자
# a -> c로 모두 옮기고 싶을 때
# 기둥에 남은 원반의 개수가 1이면 목적지 기둥으로 보내주면 된다.
# 1개 이상이면(n개) n-1를 옆기둥으로 보내주면 된다.

N = int(input())
def f(n, a, b, c):
    # print(n, a, b, c)
    if n== 1:
        print(a, c)
    else:
        f(n-1, a, c, b)
        f(1, a, b, c)
        f(n-1, b, a, c)
print(2**(N)-1)
if (N<=20):
    f(N, 1, 2, 3)