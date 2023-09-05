<<<<<<< HEAD
def qsort(arr):
    if len(arr) <=1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return qsort(left) + middle + qsort(right)

xs = qsort([3,6,8,10,1,2,1])
=======
def qsort(arr):
    if len(arr) <=1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return qsort(left) + middle + qsort(right)

xs = qsort([3,6,8,10,1,2,1])
>>>>>>> 9a90d68d7dd280c6eb2ddb8593ddd444feff7f3f
print(xs)