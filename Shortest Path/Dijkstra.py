import sys
input = sys.stdin.readline
INF = int(1e9) #무한을 의미하는 값 (10억)

n, m = map(int,input().split())   #노드의 개수 , 간선의 개수
start = int(input())        #시작 노드

array = [[] for _ in range(n+1)]    #각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
visited = [False] * (n+1)           #방문체크 (초기화)
distance = [INF] * (n+1)            #최단거리 (무한대로 초기화)

for _ in range(m) :
    a,b,c = map(int,input().split()) #a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    array[a].append((b,c))

    
def MIN() :
    min = INF
    index = 0
    for i in (1,n+1) :
        if not visited[i] and min > distance[i] :
            min = distance[i]
            index = i
    return index    


def dijkstra (start) :
    visited[start] = True
    distance[start] = 0
    
    for i in array[start] : #출발노드에서 도착노드의 비용 
        distance[i[0]] = i[1]
        
    for i in range(n-1) :
        min = MIN()
        visited[min] = True

        for j in array[min] : #출발노드에서 도착노드의 비용
            cost = distance[min] + j[i]

            if cost < distance[j[0]] :
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n+1) :
    if distance[i] == INF :
        print("INF")
    else :
        print(distance[i])

