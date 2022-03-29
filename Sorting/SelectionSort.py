#Selection Sort
import time 
from random import randint

start_time = time.time()

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# array = []
# for i in range(10000) :
#     array.append(randint(1,100))

for i in range(len(array)) :
    for j in range(i+1, len(array)) :
        if array[i] > array[j] :
            array[i], array[j] = array[j], array[i]



end_time = time.time()
print(array)
print(end_time - start_time)            