# https://programmers.co.kr/learn/courses/30/lessons/60059

def solution(key, lock):
    answer = True
    return answer


def Rotation(array) :
    length = len(array)

    result = [[0] * length for _ in range(length)] 
    for i in range(length) :
        for j in range(length) :
            result[j][length - 1- i] = array[i][j]
    return result 


x = [[0,1,0],[2,1,0],[3,1,2]]
print(Rotation(x))