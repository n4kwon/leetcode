def mergesort(arr, l, r):
    if l == r:
        return [arr[l]]
    mid = (l + r) // 2
    left = mergesort(arr, l, mid)
    right = mergesort(arr, mid + 1, r)

    return merge(left, right)

def merge(left, right):
    res = []
    i = 0
    j = 0
    while (i < len(left) and j < len(right)):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res

arr = [13, 11, 8, 1, 7, 3]
print(mergesort(arr, 0, len(arr) - 1))