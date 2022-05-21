# https://www.acmicpc.net/problem/3190

n = int(input()) #보드의 크기 N*N
k = int(input()) #사과의 개수

map_data = [[0] * (n+1) for _ in range(n+1)]
apple_array = [[0] * (n+1) for _ in range(n+1)] 

for _ in range(k) :
    a, b = map(int,input().split())
    apple_array[a][b] = 1

# 방향 관련
l = int(input()) #방향전환 횟수
way_info = []
for i in range(l) :
    x,c = input().split()
    way_info.append((int(x),c))

# 좌상우하 
dx = [-1,0,1,0]
dy = [0,-1,0,1]


def Rotation(way,direction) :
    if way == 'D' : #오른쪽 회전
        direction += 1
        if direction == 4 :
            direction = 0
    elif way == 'L' :
        direction -= 1
        if direction == -1 :
            direction = 4
    return direction

#전진 
def program() :
    # 초기상태 - 내위치,방향
    x,y = 1,1
    mx,my = 1,1
    map_data[y][x] = 1
    direction = 2
    time = 0

    for way in way_info :
        direction = Rotation(way[1],direction)

        for _ in range(way[0]) :
            my = y + dy[direction] #이동 후 좌표
            mx = x + dx[direction] #이동 후 좌표

            if my > n or my < 1 or mx > n or mx < 1 or map_data[my][mx]==2:
                return time
                
            map_data[my][mx] = 1
            time += 1

            # 사과 유무 확인
            if apple_array[my][mx] == 1 :
                apple_array[my][mx] = 0
                map_data[y][x] = 2

            elif apple_array[my][mx] == 0 :
                map_data[y][x] = 0

    return time

print(program())