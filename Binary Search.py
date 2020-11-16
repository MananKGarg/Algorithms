def binary_search(my_list, item):
    low = 0
    high = len(my_list) - 1

    while (low <= high):
        mid = (low + high) // 2
        guess = my_list[mid]

        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1

    return None

arr = [int(j) for j in input().split()]
print(binary_search(arr, 3))
