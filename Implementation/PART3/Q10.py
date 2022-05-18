# https://programmers.co.kr/learn/courses/30/lessons/60059

def solution(key, lock):
    len_key = len(key)
    len_lock = len(lock)
    len_new_lock = len_lock * 3
    
    new_lock = [[0]*len_new_lock for _ in range(len_new_lock)]
    
    # 키값 넣기
    for i in range(len_lock) :
        for j in range(len_lock) :
            new_lock[i+len_lock][j+len_lock] = lock[i][j]
    
    # 4번 돌리기
    for _ in range(4) :
        key = Rotation(key)
        
        for i in range(len_lock * 2) :
            for j in range(len_lock * 2) :
                
                #열쇠 끼우기
                for x in range(len_key) :
                    for y in range(len_key) :
                        new_lock[i+x][j+y] += key[x][y] 
                        
                        if check(new_lock) == True :
                            return True
                #열쇠 빼기
                for x in range(len_key) :
                    for y in range(len_key) :
                        new_lock[i+x][j+y] -= key[x][y] 
    return False 

def Rotation(array) :
    length = len(array)

    result = [[0] * length for _ in range(length)] 
    for i in range(length) :
        for j in range(length) :
            result[j][length - 1- i] = array[i][j]
    return result 

def check(new_lock) :
    length = len(new_lock) // 3
    
    for i in range(length, length*2) :
        for j in range(length, length*2) :
            if new_lock[i][j] != 1 :
                return False
    return True