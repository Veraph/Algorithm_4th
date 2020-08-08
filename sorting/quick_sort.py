import random

def exch(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def quick_sort(array, lo, hi):
    if hi <= lo:
        return 
    j = partition(array, lo, hi)
    quick_sort(array, lo, j-1)
    quick_sort(array, j+1, hi)


def partition(array, lo, hi):
    i = lo + 1
    j = hi
    pivot = array[lo]
    while True:
        while array[i] < pivot:
            i += 1
            if i == hi:
                break
        while array[j] > pivot:
            j -= 1
            if j == lo:
                break
        if i >= j:
            break
        exch(array, i, j)
    exch(array, lo, j)
    return j

a = [2, 3, 4, 1, 1, 2, 3, 9, 6, 5, 4, 5]
random.shuffle(a)
quick_sort(a, 0, len(a)-1)
print(a)

    
