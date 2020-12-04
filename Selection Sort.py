def findSmallest(arr):  #returns index of smallest element in array
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr): # Find the smallest element in the array and append it to a new one
    sortedArr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        sortedArr.append(arr.pop(smallest_index))
    return sortedArr

arr = [5,3,6,2,10]
print(selectionSort(arr))
