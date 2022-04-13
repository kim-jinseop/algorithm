# 순열

# 직접구현 ver

array = [1, 2, 3, 4] # n 원소 개수
r = 2                # r 뽑는 개수  
result = []

def permutation(array, r) :
    for i in range(len(array)) :
        if r == 1 :
            yield [array[i]]
        else :
            for next in permutation(array[:i]+array[i+1:], r-1) :
                yield [array[i]] + next

for i in permutation(array,r) :
    print(i, end=' ')    