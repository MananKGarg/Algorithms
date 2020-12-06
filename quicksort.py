def partition(A, l, r):
    pivot = A[l]
    j = l
    for i in range(l+1, r+1):
        if A[i] <= pivot:
            j = j + 1
            A[i], A[j] = A[j], A[i]
        
    A[j], A[l] = A[l], A[j]
    return A, j

def quicksort(A, l, r):
    if l>=r:
        return A
    else:
        A, m = partition(A,l,r)
        quicksort(A,l,m-1)
        quicksort(A,m+1,r)
    return A

arr = [10, 80, 30, 60, 60, 60, 70]
print(quicksort(arr, 0, len(arr)-1))
