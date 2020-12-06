'''Though this implementation of quicksort looks simpler and more intuitive than the original in the Algorithms repository,
this is a slightly worse quicksort than the other one. It is because here, we create new subarrays at every call
 which we didn't do there. But this looks neat'''

def quicksort(arr):
    if len(arr) < 2:          # (Base case) Arrays with lengths 0 or 1 are already sorted
        return arr
    else:
        pivot = arr[0]        # leftmost element as pivot
        less = [i for i in arr[1:] if i <= pivot]       
        greater = [i for i in arr[1:] if i > pivot]     
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([2,8,4,4,78,78,23,45]))
