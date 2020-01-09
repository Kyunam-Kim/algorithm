import random
import time

def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def pivotFirst(x, left, right):
    pivot_val = x[left]
    pivot_idx = left
    while left <= right:
        while left <= right and x[left] <= pivot_val:
            left += 1
        while left <= right and x[right] >= pivot_val:
            right -= 1
        if left <= right:
            swap(x, left, right)
            left += 1
            right -= 1
    swap(x, pivot_idx, right)
    return right

def quickSort(x, pivotMethod=pivotFirst):
    def _qsort(x, first, last):
        if first < last:
            splitpoint = pivotFirst(x, first, last)
            _qsort(x, first, splitpoint-1)
            _qsort(x, splitpoint+1, last)
    _qsort(x, 0, len(x) - 1)
 
if __name__=='__main__':
    list = []
    input_n = input("data number: ")
    for i in range(int(input_n)):
        list.append(random.randint(1,int(input_n)))
    print("Before sort")
    print(list)

    start_time = time.time()
    quickSort(list)
    running_time = time.time() - start_time

    print("After sort")
    print(list)

    print("data size: {}".format(int(input_n)))
    # print("compare counter: {}".format(compare_counter))
    # print("swap counter: {}".format(swap_counter))
    print("running time: {}".format(running_time))