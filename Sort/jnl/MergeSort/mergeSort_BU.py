## BOTTOM UP 방식: 재귀x , 반복 o
# TD 방식과는 다르게 tmp를 수정해줘야 한다.
# 참고로 TD 방식에선 mergeSort()함수가 재귀적으로 호출되어서 tmp가 갱신된 arr을 복사한 것으로 최신화된다.
# 반면 BU 방식에선 재귀가 아니라 반복이 사용되므로, for문이 돌때마다 merge()함수가 반복적으로 호출되고, merge() 함수 내에서 비교 중간중간 tmp를 사용해 저장해두고, 마지막에 arr에 다시 넣어주는 식으로 구현해햐 한다.
import copy

cnt = 0
def merge(arr, tmp, start, mid, end):
    global cnt
    cnt += 1  

    part1 = start #0 #2 //#0 //#0
    part2 = mid+1 #1(end=1) #2(end=3) //#3(end=3) //#5
    i = start #0 #2 //#0 //$0
    
    while part1 <= mid and part2 <= end:
        if arr[part1] < arr[part2]:
            tmp[i] = arr[part1]
            part1 += 1
        else:
            tmp[i] = arr[part2]
            part2 += 1
        i += 1

    while part1 <= mid:
        tmp[i] = arr[part1]
        i += 1
        part1 += 1
    # tmp = [5, 7, 3, -9, -4] # tmp = [5, 7, -9, 3, -4] // #tmp=[3, -]
     
    # tmp를 arr로 다시 복사
    for i in range(start, end+1):
        arr[i] = tmp[i]
    
       
    

def mergeSort(arr):
    start = 0
    end = len(arr)-1 #end = 4

    tmp = copy.deepcopy(arr)

    m = 1 # 서브리스트의 크기(1 -> 2 -> 4 -> 8 ...)
    # 반복문 돌아가는 조건: 서브리스트의 크기가 전체리스트 길이보다 작거나 같을 때
    while m <= end-start:
        # 2*m : 크기가 m인 서브리스트 두개를 합쳐줄거라
        # 서브리스트의 크기는 2배씩 증가한다

        for i in range(start, end, 2*m):
            low = i 
            mid = i + m - 1
            high = min(i+2*m-1, end)
            merge(arr, tmp, low, mid, high) 
            #m=1
                #i = 0: (0, 0, 1)-> arr = tmp =[5, 7, 3, -9, -4]
                #i = 2: (2, 2, 3)-> arr = tmp = [5, 7, -9, 3, -4]
            #m=2
                #i = 0: (0, 1, 3)-> arr = tmp = [-9, 3, 7, -9, -4]
            #m=4
                #i = 0: (0, 4, 4)
        
        m = 2*m

A = [5, 7, 3, -9, -4, 2, 8]
mergeSort(A)
print(A)