def validMountainArray(arr):
    if len(arr) < 3:
        return False
    i = 0
    while i < len(arr) and i + 1 < len(arr) and arr[i] < arr[i + 1]:
        i += 1

    if i == 0 or i + 1 >= len(arr):
        return False

    while i < len(arr) and i + 1 < len(arr):
        if arr[i] <= arr[i + 1]:
            return False
        i += 1

    return True


print(validMountainArray([1]))
