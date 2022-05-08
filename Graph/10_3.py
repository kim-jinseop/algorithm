# Curriculum

''' input data

5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

'''

from collections import deque
import copy

n = int(input()) #강의의 수

# 진입 차수 0 으로 초기화
indegree = [0] * (n+1)

# 간선 정보 저장용 리스트 초기화
array = [[] for _ in range(n+1)]

# 시간 정보
time = [0] * (n+1)

for i in range(1,n+1) :
    data = list(map(int,input().split()))
    time[i] = data[0]

    for j in data[1:-1] :
        indegree[i] += 1
        array[j].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1,n+1) :
        if indegree[i]==0 :
            q.append(i)

    while q :
        now = q.popleft()
        
        for i in array[now] :
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1
                 
            if indegree[i] == 0 :
                q.append(i)

    for i in range(1, n+1) :
        print(result[i])

topology_sort()                    