N,K = map(int,input().split())
count = 0

while N>=K :
    if N%K==0 :
        count = count + 1
        N = N//K
    else :
        count = count + 1
        N -= 1

while N!=1 :
    count = count + 1
    N -= 1

print(count)         