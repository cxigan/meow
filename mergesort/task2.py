def sum_digits(n):
    total = 0
    for d in str(n):
        total += int(d)
    return total


def merge(left, right):
    res = []

    while left and right:
        if sum_digits(left[0]) <= sum_digits(right[0]):
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))

    return res + left + right


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    m = len(arr) // 2
    return merge(merge_sort(arr[:m]), merge_sort(arr[m:]))


arr = [105, 22, 1001, 45, 12]

print(merge_sort(arr))
