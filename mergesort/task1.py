count = 0

def merge(left, right):
    global count
    res = []

    while left and right:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            count += len(left)
            res.append(right.pop(0))

    return res + left + right


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    m = len(arr) // 2
    return merge(merge_sort(arr[:m]), merge_sort(arr[m:]))


arr = [2, 4, 1, 3, 5]

print(merge_sort(arr))
print(count)
