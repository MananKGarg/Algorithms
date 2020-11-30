def mergesort(arr):
    if(len(arr) == 1):
        return arr
    else:
        m = len(arr)//2
        b = mergesort(arr[:m])
        c = mergesort(arr[m:])
        d = merge(b,c)
    return d

def merge(b,c):   # b and c are already sorted
    d = []
    while(len(b)>0 and len(c)>0):
        if(b[0]<=c[0]):
            d.append(b[0])
            b.pop(0)
        else:
            d.append(c[0])
            c.pop(0)
    if(len(b)>0):
        d.extend(b)
    else:
        d.extend(c)
    return d

arr = [2,6,1,3,5,4]
d = mergesort(arr)
print(d)

