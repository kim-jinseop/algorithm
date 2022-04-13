# 순열

array = [1, 2, 3, 4] # n 원소 개수
r = 2                # r 뽑는 개수  

from itertools import permutations

per = list(permutations(array,r))
print(per)


# 중복순열

array = [1, 2, 3, 4] # n 원소 개수
r = 2                # r 뽑는 개수  

from itertools import product

per = list(product(array,repeat = r))
print(per)