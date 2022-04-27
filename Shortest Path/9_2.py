#전보 
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n , m , start = map(int,input().split()) #도시(노드)의 개수, 통로(간선)의 개수

array = [[] for _ in range(n+1)] #각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트

distance = [INF] * (n+1) #거리 정보를 담는 리스트 값은 무한으로 

for _ in range(m) :
    a,b,c = map(int,input().split())
    array[a].append((b,c)) #a번 노드에서 b번 노드로 가는데 사용된 비용 c 
    
def dijkstra(start) :
    q = []
    heapq.heappush(q,(0,start)) #비용,노드
    distance[start] = 0
    
    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue    

        for i in array[now] :
            
            cost = dist + i[1]
           
            if cost < distance[i[0]] :
                distance[i[0]] = cost           
                heapq.heappush(q,(cost,i[0]))
                
dijkstra(start)           
                                   
#총걸리는 시간 : 가장멀리있는 노드
count = 0
max_distance = 0

for d in distance :
    if d != INF :
        count += 1
        max_distance = max(max_distance, d)

#시작노드 제외해야 하기 때문에 count - 1         
print(count-1, max_distance)        