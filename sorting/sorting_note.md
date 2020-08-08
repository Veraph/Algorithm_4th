# Sorting Notes
## Elementary Sorts
### Selection Sort
For a array of N elements, loop the array N times to find the smallest one to swap with the left(N-n) one  
Time complexity O(n^2)

    array = [7, 3, 2, 5, 6, 8, 0, 1]

    len_array = len(array)
    for i in range(len_array):
        start_index = i
        min_index = i
        for j in range(i, len_array):
            if array[min_index] > array[j]:
                min_index = j

        temp = array[start_index]
        array[start_index] = array[min_index]
        array[min_index] = temp

### Insertion Sort
Insertion sort is useful when sorting the partially sorted array(number of inversions is low).
Time complexity O(n^2)

    for i in range(1, len_array):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                temp = array[j-1]
                array[j-1] = array[j]
                array[j] = temp

### Shell Sort
Based on insertion sort, but allow the exchanges of array entries that are far apart.  
Normally use the increment sequence of 3n+1 (1, 4, 13, 40...), useful for large array
Approximately Time complexity O(n^2) but faster than previous two

    h = 1
    while h < len_array / 3:
        h = 3*h + 1
    while h >= 1:
        for i in range(h, len_array):
            for j in range(i, h, -h):
                if array[j] < array[j-h]:
                    temp = array[j-h]
                    array[j-h] = array[j]
                    array[j] = temp

## Merge Sort
Time Complexity O(nlogn)
Use extra space proportional to N
It is a prototype of Divide and Conquer algorithm
### Top-down Merge

    # recursively done this job
    def merge(array, lo, mid, hi):
        aux = array[:hi+1] # be careful that the slice copy do not copy the index to the right of :
        l = lo, m = mid + 1
        for i in range(lo, hi+1):
            if l > mid:
                array[i] = aux[m]
                m += 1
            elif m > hi:
                array[i] = aux[l]
                l += 1
            elif aux[l] > aux[m]:
                array[i] = aux[m]
                m += 1
            else:
                array[i] = aux[l]
                l += 1

    def merge_sort(array, lo, hi):
        mid = int(lo + (hi - lo) / 2)
        if hi <= lo:
            return
        sort(array, lo, mid)
        sort(array, mid+1, hi)
        merge(array, lo, mid, hi)
    
    merge_sort(array, 0, len(array)-1)

### Bottom-up Merge

    # instead of solve a big problem by dividing it into pieces, BU_merge do all the merges of tiny subarrays on one pass then do a second pass...
    def BU_merge_sort(array):
        for sz in range(1, len(array), sz):
            for lo in range(0, N-sz, sz+sz):
                merge(array, lo, lo+sz-1, min(lo+sz+sz-1, N-1))

## Quick Sort
Time complexity average: O(nlogn)
Space: in-space
Divide-and-conquer method  
Do much less data movement than merge sort

    # out-space quick sort
    import random
    array = [4, 5, 2, 4, 9, 1, 3, 8]
        
    def quick_sort(array):
        random.shuffle(array)
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        more = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(more)

    # This method is problematic becasue it use lots of addition space, we could do the quick sort in space.

## Priority Queues
support two operations: remove the maximum and insert