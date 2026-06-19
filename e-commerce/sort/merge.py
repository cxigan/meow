def _merge(arr, left, mid, right, compare):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]
    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if compare(left_part[i], right_part[j]) <= 0:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


def _merge_sort(arr, left, right, compare):
    if left < right:
        mid = (left + right) // 2
        _merge_sort(arr, left, mid, compare)
        _merge_sort(arr, mid + 1, right, compare)
        _merge(arr, left, mid, right, compare)


def sort(arr, compare):
    _merge_sort(arr, 0, len(arr) - 1, compare)
    return arr
