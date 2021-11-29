'''
QuickSort:
Time:
    Average case: 0(NlgN) assuming randomized array that the partition always ends up in the middle(hard)
    Worst Case: 0(N^2) on a sorted array(partition index always at the same index so n partitions trees(linkedlist) (not lg n))
                so it becomes n*n
Space:
lg n to N(determined by height of partition tree ie what items on tree at some time)
'''
import random


def partition(arr, l, h):
    pivot = l
    i, j = l, h
    while i < j:
        while i < len(arr) and arr[i] < arr[pivot]:
            i += 1
        while j >= i and arr[j] > arr[pivot]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1

    arr[pivot], arr[j] = arr[j], arr[pivot]
    return j


def quicksort(arr, l, h):
    if l >= h:
        return
    p = partition(arr, l, h)
    quicksort(arr, l, p)
    quicksort(arr, p+1, h)
    return arr


arr = [random.randint(0, 1000) for _ in range(20)]
print(arr)
sorted_arr = quicksort(arr, 0, len(arr)-1)
print(sorted_arr == sorted(arr))
