#game development

# input
n,m = map(int,input().split())
x, y, direction = map(int,input().split())

# map init
d = [[0] * m for _ in range(n)] #list comprehension

# my position check
d[x][y] = 1

# imput map data
array = []
for i in range(n) :
   array.append(list(map(int,input().split())))

# Direction init
# North, East, South, West
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# Rotation function
def turn_left() :
   global direction
   direction -= 1

   if direction == -1 :
      direction = 3

# action
count = 1 #방문한 칸의 수
turn_cnt = 0 #회전한 수

while True :
   turn_left()

   nx = dx[direction] + x
   ny = dy[direction] + y

   # 육지일 때 
   if d[nx][ny] == 0 and array[nx][ny] == 0 : 
      d[nx][ny] = 1

      x = nx
      y = ny

      count += 1
      turn_cnt = 0

      continue #바로 while 문으로

   # 바다일 때
   else :
      turn_cnt += 1

   # 네면 모두 갈 수 없을 때
   if turn_cnt==4 : 
      nx = x - dx[direction]
      ny = y - dy[direction]

      if array[nx][ny] == 1 :
         break
      else :
         x = nx
         y = ny
      turn_cnt = 0


print(count)