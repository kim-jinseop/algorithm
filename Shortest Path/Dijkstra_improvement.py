#que를 이용한 dijkstra
#우선순위 큐(priority Queue)
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split()) # n: 노드 개수 / m: 간선 개수
start = int(input()) # 시작 노드 번호

array = [[] for _ in range(n+1)]
for _ in range(m) :
    a,b,c = map(int,input().split())
    array[a].append((b,c)) # a번 노드에서 b번 노드로 가는 비용 c
    
distance = [INF] * (n+1)   # 거리


def dijkstra(start) :
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    while q :
        dist, now = heapq.heappop(q) # 최단거리 노드정보
        
        if distance[now] < dist :
            continue
        
        for i in array[now] : # i[0] : b(노드) / i[1] : c(비용)
            cost = dist + i[1]
            
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
                
    
dijkstra(start)


for i in range(1,n+1) :
    if distance[i]==INF :
        print("INF")
    else :
        print(distance[i])