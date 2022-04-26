INF = int(1e9)

n = int(input()) #노드의 개수
m = int(input()) #간선의 개수

#2차원 그래프를 만드고 INF로 초기화
array = [[INF] * (n+1) for _ in range(n+1)] #리스트 컴프리핸션

#자기자신으로 가는 비용을 0으로 초기화
for i in range(1,n+1) :
    array[i][i] = 0

#간선에 대한 정보 입력
for i in range(m) :
    a,b,c = map(int,input().split())
    array[a][b] = c
        

# 출력
for i in range(1,n+1) :
    for j in range(1,n+1) :
        print(array[i][j],end=' ')
    print()    