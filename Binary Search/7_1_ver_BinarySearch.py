def binary_search (array, target, start, end) :
    if start > end :
        return None
    
    mid = (start + end) // 2 
    
    if target == array[mid] :
        return mid
    elif target > array[mid] :
        return binary_search (array, target, mid+1, end)
    else :
        return binary_search (array, target, start, mid-1)
    
n = int(input())
array_n = list(map(int,input().split()))
m = int(input())
array_m = list(map(int,input().split()))

array_n.sort()

for i in range(m) :
    result = binary_search(array_n, array_m[i], 0, n-1 )
    if result == None :
        print("No",end=" ")
    else : 
        print("Yes",end=" ")