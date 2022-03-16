n, m, k = map(int,input().split())
data = list(map(int,input().split()))

data.sort(reverse=True)

max = data[0]
max_2 = data[1]

i = 1
result = 0

while i<=m :

    if i%(k+1)==0 :
        result = result + max_2
    else :
        result = result + max 
    
    i += 1
    print(result)


print("답:" + str(result))