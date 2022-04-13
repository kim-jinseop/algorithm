# 조합

array = [1, 2, 3, 4] # n 원소 개수
r = 2                # r 뽑는 개수  

from itertools import combinations

per = list(combinations(array,r))
print(per)

# 중복조합

array = [1, 2, 3, 4] # n 원소 개수
r = 2                # r 뽑는 개수  

from itertools import combinations_with_replacement

per = list(combinations_with_replacement(array,r))
print(per)