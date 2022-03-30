array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def Quick_Sort(array, start, end) :

    pivot = start    # 피벗 설정
    East = pivot + 1 # 오른쪽으로 이동
    West = end       # 왼쪽으로 이동 

    if start >= end : # 리스트가 1개 일때 
        return

    while True :
        # 피벗보다 큰값 찾기
        while East <= end  and array[pivot] >= array[East] :
            East += 1 
        # 피벗보다 작은값 찾기
        while West > start and array[pivot] <= array[West] :
            West -= 1
         
        # 값이 서로 엇갈릴 때 
        if East > West :
            array[pivot], array[West] = array[West], array[pivot]
            break
        # 안 엇갈린 상황에서 교환
        else :
            array[East], array[West] = array[West], array[East]

    #재귀 함수 -> 분할된 리스트 왼쪽 오른쪽 다시 퀵 정렬 수행
    Quick_Sort(array,start,West-1)
    Quick_Sort(array,West+1,end)


Quick_Sort(array,0,len(array) - 1)

print(array)

