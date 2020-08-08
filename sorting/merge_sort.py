def merge(array, lo, mid, hi):
        aux = array[:hi+1]
        l = lo
        m = mid+1
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
    merge_sort(array, lo, mid)
    merge_sort(array, mid+1, hi)
    merge(array, lo, mid, hi)

array = [3, 4, 2, 3, 1, 8, 7, 9, 0]
merge_sort(array, 0, len(array)-1)
print(array)


def BU_merge_sort(array):
    len_array = len(array)
    sz = 1
    while sz < len(array):
        for lo in range(0, len_array-sz, sz+sz):
            merge(array, lo, lo+sz-1, min(lo+sz+sz-1, len_array-1))
        sz += sz
array1 = [3, 4, 2, 3, 1, 8, 7, 9, 0]
BU_merge_sort(array1)
print(array1)
