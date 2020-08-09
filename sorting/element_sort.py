import time

array = [7, 3, 2, 5, 6, 8, 0, 1]
len_array = len(array)

def exch(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

# Selection sort
array1 = array[:]
start_time = time.time()

for i in range(len_array):
    start_index = i
    min_index = i
    for j in range(i, len_array):
        if array1[min_index] > array1[j]:
            min_index = j
    temp = array1[start_index]
    array1[start_index] = array1[min_index]
    array1[min_index] = temp

time_consumped = time.time() - start_time
print('selection sort: %s' % time_consumped)
print(array1)

# Insertion sort
array1 = array[:]
start_time = time.time()

for i in range(1, len_array-1):
    j = i
    while (j > 0 and array1[j] < array1[j-1]):
        exch(array1, j, j-1)
        j -= 1

time_consumped = time.time() - start_time              
print('insertion sort: %s' % time_consumped)
print(array1)

# Shell sort
array1 = array[:]
start_time = time.time()

h = 1
while h < len_array / 3:
    h = h*3 + 1
while h >= 1:
    for i in range(h, len_array-1):
        j = i
        while (j >= h and array1[j] < array1[j-h]):
            exch(array1, j, j-h)
            j -= h
    h = int(h/3)

time_consumped = time.time() - start_time              
print('shell sort: %s' % time_consumped)
print(array1)