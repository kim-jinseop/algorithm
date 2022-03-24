#Imperial Night

#Input data
from unittest import result


point = input()
xp = int(point[1])
yp = ord(point[0]) - ord('a') + 1

#move
move = [(-2,-1), (-2,1), (2,-1), (2,1),
        (-1,-2), (-1,2), (1,-2), (1,2),]

result = 0
for i in range(len(move)) :
    dx = xp + move[i][0]
    dy = yp + move[i][1]

    if(dx>=1 or dx<=8 or dy>=1 or dy<=8) :
        result += 1
                
print(result)