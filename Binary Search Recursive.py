def binary_search_recursive(arr, item, low, high):
    if low > high:
        return None
    mid = (low + high)//2
    if arr[mid] == item:
        return mid
    elif arr[mid] < item:
        return binary_search_recursive(arr, item, mid+1, high)
    elif arr[mid] > item:
        return binary_search_recursive(arr, item, low, mid - 1)

arr = [1,3,7,9,23,45,78]
print(binary_search_recursive(arr, 8, 0, 6))
