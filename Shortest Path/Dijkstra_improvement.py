#que를 이용한 dijkstra
#우선순위 큐(priority Queue)
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())

array = [[] for _ in range(n+1)]
for _ in range(m) :
    a,b,c = map(int,input().split())
    array[a].append((b,c))
    
vitsited = [False] * (n+1)
distance = [INF] * (n+1)


def dijkstra(start) :
    
    return

    
dijkstra(start)


    