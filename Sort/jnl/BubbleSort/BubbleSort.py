from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]



# 개선 1
# 모든 원소에 대해 비교를 하기 전에 배열이 모두 정렬된 경우 -> 더이상 비교는 의미 없게 된다.
def bubble_sort_advanced_1(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n-1):
        exchange_cnt = 0
        for j in range(i+1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                exchange_cnt += 1
        
        if exchange_cnt == 0:
            break

# 개선 2
# 비교대상이 되는 인덱스의 범위를 제한해 비교의 횟수를 줄임
def bubble_sort_advanced_2(a:MutableSequence) -> None:
    n = len(a)
    k = 0
    while k < n-1:
        last = n-1
        for j in range(n-1, k, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        k = last


# 셰이커 정렬
# 양방향 버블 정렬
# 홀수 패스에서는 가장 작은 원소를 맨 앞으로 이동
# 짝수 패스에서는 가장 큰 원소를 맨 뒤로 이동
def shaker_sort(a: MutableSequence) -> None:
    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        # 홀수 패스
        for i in range(right, left, -1):
            if a[i-1] > a[i]:
                a[i-1], a[i] = a[i], a[i-1]
                last = i
        left = last

        #짝수 패스
        for j in range(left, right):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                last = j
        right = last

