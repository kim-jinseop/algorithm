# BFS
from collections import deque

# input
n, m = map(int,input().split())

graph = []
for _ in range(n) :
    graph.append(list(map(int,input().split())))

# position
dx = [-1,0,1,0] 
dy = [0,-1,0,1] #북서남동

# create queue
queue = deque()  
    
# bfs func   
def bfs(x, y) :  
    queue.append((x,y)) #큐에 처음 노드를 넣는다.
    
    while queue :
        x, y = queue.popleft() #방문 처리된 노드는 빼준다
        
        for i in range(4) : #북서남동 4회 탐색
            nx = dx[i] + x
            ny = dy[i] + y
        
            if nx < 0 or nx >= n or ny < 0 or ny >= m : #범위를 벗어나면 다음 반복문 실행 
                continue
            
            if graph[nx][ny] == 0 : #막혀있는 곳이라면 다음 반복문 실행
                continue
                         
            if graph[nx][ny] == 1 : #다음 지나가는방을 발견할 때
                graph[nx][ny] = graph[x][y] + 1 
                queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0, 0))