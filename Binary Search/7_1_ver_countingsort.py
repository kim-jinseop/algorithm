n = int(input())
array_n = [0] * 1000001

for i in input().split() :
    array_n[int(i)] = 1

m = int(input())
array_m = map(int,input().split())   

for i in array_m :
    if array_n[i] == 1 :
        print("yes", end=" ")
    else : 
        print("no",end=" ")
