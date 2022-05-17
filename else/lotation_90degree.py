# 리스트를 +90도 회전

def Rotation(array) :
    length = len(array)

    result = [[0] * length for _ in range(length)] 
    for i in range(length) :
        for j in range(length) :
            result[j][length - 1 - i] = array[i][j]
    return result 

