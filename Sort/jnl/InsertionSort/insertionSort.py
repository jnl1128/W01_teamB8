from typing import MutableSequence

def insertion_sort(a:MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        j = i
        target = a[i]
        while j > 0 and a[j-1] > target:
            a[j] = a[j-1]
            j -= 1
        a[j] = target

# 개선
# 이진 삽입 정렬
# 배열의 원소 수가 많아지면 비교/교환 비용이 커진다.
# 이진 삽입 정렬 -> 이미 정렬을 마친 배열을 제외하고 원소를 삽입해야 할 위치를 검사 -> 비용 감소
def binary_insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        target = a[i]
        pl = 0 #비교대상의 시작 index
        pr = i-1 #비교대상의 끝 index

        while True:
            pc = (pl+pr)//2
            if a[pc] == target:
                break
            elif a[pc] < target:
                pl = pc + 1
            else:
                pr = pc -1
            
            if pl > pr:
                break
        
        pd = pc + 1 if pl <= pr else pr + 1

        for j in range(i, pd, -1):
            a[j] = a[j-1]

        a[pd] = target