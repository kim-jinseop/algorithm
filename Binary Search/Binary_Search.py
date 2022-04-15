def Binary_search (target, array, start, end) :
    if start>end :
        return None
    
    mid = (start + end) // 2 
    
    if target == array[mid] :
        return mid
    elif target > array[mid] :
        return Binary_search (target, array, mid+1, end)
    elif target < array[mid] :
        return Binary_search (target, array, start, mid-1)      
        
n, target = map(int,input().split()) # n(원소의 개수), target(찾고자 하는 문자열)
array = list(map(int,input().split()))

result = Binary_search(target, array, 0, n-1)

if result == None:
    print("원소가 존재하지 않음")
else :
    print(result+1)
    

