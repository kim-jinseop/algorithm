n = int(input())
array_n = set(map(int,input().split()))
m = int(input())
array_m = map(int,input().split())

for i in array_m :
    if i in array_n :
        print("yes",end=" ")
    else : 
        print("no",end=" ")