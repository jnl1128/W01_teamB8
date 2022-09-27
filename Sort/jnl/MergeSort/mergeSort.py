# python에서 sorted()가 병합정렬임.
    # sorted() 함수는 이미 정렬되어 있지 않은 리스트를 인자를 받아도 정렬해줌
    # 하지만 시간이 오래걸림
    # 시간을 줄이기 위해 : heapq 모듈의 merge() 함수 사용할 수 있음 ex) heapq.merge(a,b)
    # using heapq is faster than sorting with list, when it comes to adding new elements on the fly(== unspecified length)
# 시간복잡도: O(nlogn)
    # 배열을 병합할 때는 O(n)만큼의 시간이 들지만
    # 정렬의 단계가 logn만큼 필요하므로
    # 전체 시간복잡도: O(nlogn)


# 병합 정렬
    # 정렬을 마친 배열의 병합을 응용해서, 분할 정복법에 따라 정렬하는 알고리즘

# 병합 정렬 알고리즘    
    # 배열의 원소 수가 2개 이상일 경우
        # 1. 배열의 앞부분을 병합 정렬로 정렬
        # 2. 배열의 뒷부분을 병합 정렬로 정렬
        # 3. 배열의 앞부분과 뒷부분을 병합

from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None:

    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        if left < right:
            center = (left+right)//2

            _merge_sort(a, left, center) # 앞부분 정렬
            _merge_sort(a, center+1, right) # 뒷부분 정렬


            # 현재 정렬해줄 부분의 시작 인덱스 left / 끝 인덱스 right
            # 앞부분과 뒷부분 병합 과정: buffer를 사용해 앞부분과 뒷부분을 병합
            p = j = 0 # p: buffer 포인터
            i = k = left

            # 앞부분(left~center)을 buffer(0~center-left)에 복사하기 
            # while이 끝날 때 p == center-left+1 == 복사한 원소 수
            # p와 i는 정렬된 앞부분을 buffer에 저장시키고자 +1 해주는 변수
            while i <= center:
                buffer[p] = a[i]
                p += 1
                i += 1

            # "뒷부분(center+1~right)"과 "buffer로 복사한 배열의 앞부분 p개를 병합한 결과"를 배열 a에 저장
            # i : left~right 사이에 있는 인덱스
            # k : a 배열에 다음으로 삽입할 부분을 가리키는 포인터
            # j : buffer에 이미 복사되어 있는 앞부분을 가리키는 포인터
            # i <= right : 아직 a 끝까지 다 본거 아니라면
            # "앞부분은 이미 buffer에 정렬"해둔 상태고, 총 p개 정렬된 상태임
                # 비교를 해야 하므로 j<p로 범위 조건을 만들어 둠
            while i<=right and j < p:
                if buffer[j] <= a[i]:
                    a[k] = buffer[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1
        
            # 앞부분에 정렬된 부분이 남았을 경우
            while j < p:
                a[k] = buffer[j]
                k += 1
                j += 1




            

    n = len(a)
    # buffer: _merge_sort()입장에서 보면 전역변수
    buffer = [None]*n # 작업용 배열(병합 결과를 임시저장하는 작업용 배열)을 생성
    _merge_sort(a, 0, n-1) # 배열 전체를 병합정렬: 실제적으로 정렬 과정을 실행하는 _merge_sort()를 실행
    del buffer # 작업용 배열을 소멸
