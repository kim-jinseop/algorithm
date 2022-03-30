'''
시간복잡도 : O(N^2) 

선택정렬과 흡사한 시간 소요
but 정렬이 어느정도 되어있는 상태라면 매우 빠르게 동작한다.
최선의 경우 O(N)의 시간복잡도를 가진다.
'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1,len(array)) :
    for j in range(i,0,-1) :   
        if array[j] < array[j-1] :
            array[j], array[j-1] = array[j-1], array[j]
        else :
            break

print(array)