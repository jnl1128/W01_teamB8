## TOP DOWN 방식

import copy
# 결합
def merge(arr,tmp,start, mid, end):
    tmp = copy.deepcopy(arr)

    part1 = start
    part2 = mid + 1
    i = start

    while part1 <= mid and part2 <= end:
        if(tmp[part1] <= tmp[part2]):
            arr[i] = tmp[part1]
            part1 += 1
        else:
            arr[i] = tmp[part2]
            part2 += 1
        i += 1

    while part1 <= mid:
        arr[i] = tmp[part1]
        part1 += 1
        i += 1


# 분할+정복
    # 분할: 정렬되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
    # 정복: 각 부분 리스트를 재귀적으로 합변 정렬을 이용해 정렬한다 
def mergeSort(arr, tmp, start, end):
    if (start<end):
        mid = (start+end)//2 
        # 앞부분                                                                                                                  
        mergeSort(arr, tmp, start, mid)
        # 뒷부분
        mergeSort(arr, tmp, mid+1, end)
        # 위의 두 함수를 호출한 후에는 mid를 기준으로 앞부분끼리,뒷부분끼리 정렬된 상태
        merge(arr, tmp, start, mid, end)

# [4, 22, 106, 8, 11]
a = [22, 4, 106, 8, 11]
mergeSort(a, [], 0, len(a)-1)

# print(a)




