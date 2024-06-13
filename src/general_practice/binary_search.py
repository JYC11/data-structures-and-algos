array = [i for i in range(1000)]


def binary_search_v1(array, item):  # using a simple while loop
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        print(array[mid])
        if array[mid] == item:
            return mid
        if array[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def binary_search_v2(array, item, low, high):  # using recursion
    if low > high:
        return None
    else:
        mid = (low + high) // 2
        print(array[mid])
        if array[mid] == item:
            return mid
        elif array[mid] > item:
            binary_search_v2(array, item, low, mid - 1)
        else:
            binary_search_v2(array, item, mid + 1, high)
    return None


def binary_search_group(arr, target):
    left_index = -1
    right_index = -1

    # looking for the leftmost index of the target
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            left_index = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # looking for the rightmost index of the target
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            right_index = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return [left_index, right_index]
