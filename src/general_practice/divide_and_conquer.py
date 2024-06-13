def dnc_array_sum(array):
    summed = 0
    if len(array) == 0:
        return 0
    else:
        summed = array[0] + sum(array[1:])
        dnc_array_sum(array[1:])
    return summed


array = [33, 452, 53, 11, 6675, 14, 66]


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[i]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[i]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
