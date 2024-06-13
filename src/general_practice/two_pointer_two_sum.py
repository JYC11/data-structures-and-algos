def two_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] + arr[right] < target:
            left += 1
        elif arr[left] + arr[right] > target:
            right -= 1
        else:
            return [left, right]

    return [-1, -1]
