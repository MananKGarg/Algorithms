import random

def partition3(a, l, r):
    x = a[l]
    j = l
    k = l

    for i in range(l+1, r+1):
        if x == a[i]:
            k += 1
            a[i], a[k] = a[k], a[i]
        elif a[i] < x:
            j += 1
            k += 1
            a[i], a[k] = a[k], a[i]
            a[j], a[k] = a[k], a[j]
    a[l], a[j] = a[j], a[l]
    return a, j, k

def randomized_quick_sort(a, l, r):
    if l >= r:
        return a
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    a, m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)
    return a
arr = [3,4,5,3,7,2,9,2,2,3,6,7]
print(randomized_quick_sort(arr,0,len(arr)-1))
