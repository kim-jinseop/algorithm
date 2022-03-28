from collections import deque
from turtle import Turtle

def BFS(graph, start, visited) :
    queue = deque([start])
    visited[start] = True

    # q 가 빌때까지 반복
    while queue :
        # q 에서 원소를 하나 뽑아서 출력
        v = queue.popleft() 
        print(v, end=' ')
        
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [0] * 9

BFS(graph, 1, visited)   