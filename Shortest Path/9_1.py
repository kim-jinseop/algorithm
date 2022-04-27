#City of the future
INF = int(1e9)

n , m = map(int,input().split()) #회사(노드)의 개수, 경로(간선)의 개수

array = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m) :
    a,b = map(int,input().split())    
    array[a][b] = 1
    array[b][a] = 1
    
#자기자신으로 가는 횟수 0
for i in range(1,n+1) :
    array[i][i] = 0
       
x , k = map(int,input().split()) # 1번째 도착지점 k , 2번째 도착지점 x


#플로이드 위셜 알고리즘 수행
for k in range(n+1) :
    for a in range(n+1) :
        for b in range(n+1) :
            array[a][b] = min(array[a][b], array[a][k]+array[k][b])
            
#원하는 경로 추출
distance = array[1][k] + array[k][x]            

if distance==INF :
    print("-1")
else :      
    print(distance)    