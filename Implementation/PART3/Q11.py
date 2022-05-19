# https://www.acmicpc.net/problem/3190

n = int(input()) #보드의 크기 N*N
k = int(input()) #사과의 개수

map = [[0] * (n+1) for _ in range(n+1)]
apple_array = [[0] * (n+1) for _ in range(n+1)] 

for _ in range(k) :
    a,b = map(int,input().split())
    apple_array[a][b] = 1

l = int(input()) #방향전환 횟수

way_info = []
for i in range(l) :
    x,c = map(int,input().split())
    way_info.append((x,c))

#좌상우하 
dx = [-1,0,1,0]
dy = [0,-1,0,1]

# 초기상태 - 내위치,방향
x,y = 1
mx,my = 1
map[y][x] = 1
diretion = 2

for way in way_info :
    if way[1] == 'D' : #오른쪽 회전
        diretion += 1
        if diretion == 4 :
            diretion = 0
    elif way[1] == 'L' :
        diretion -= 1
        if diretion == -1 :
            diretion = 4

    #전진 
    for _ in range(way[0]) :
        my = y + dy[diretion] #이동 후 좌표
        mx = x + dx[diretion] #이동 후 좌표
        map[my][mx] = 1

        if apple_array[my][mx] == 1 :
            apple_array[my][mx] = 0
        elif apple_array[my][mx] == 0 :
            map[y][x] = 0
