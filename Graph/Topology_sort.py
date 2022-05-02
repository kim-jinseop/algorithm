# 위상정렬 : 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘
from collections import deque

#노도의 개수와 간선 개수 입력받기
v , e = map(int,input().split())
#진입차수 초기화 '0'으로 
indegree = [0] * (v+1)
#간선정보를 저장하기 위한 리스트 초기화
array = [[] for _ in range(v+1)]

for i in range(e) :
    a,b = map(int,input().split())
    array[a].append(b)
    indegree[b] += 1


def topology_sort() :
    result = []
    q = deque()

    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1) :
        if indegree[i] == 0 :
            q.append(i)

    while q :
        now = q.popleft()
        result.append(now)

        for i in array[now] :
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)
    
    for i in result :
        print(i,end=' ')

topology_sort()

