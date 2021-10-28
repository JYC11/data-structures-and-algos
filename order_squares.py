def order_squares(arr):
    right = 0
    while right < len(arr) and arr[right] < 0:
        right += 1
    left = right -1

    output = []

    while left >= 0 and right < len(arr):
        if arr[left]**2 < arr[right]**2:
            output.append(arr[left]**2)
            left -= 1
        else:
            output.append(arr[right]**2)
            right += 1
    while left >= 0:
        output.append(arr[left]**2)
        left -= 1
    while right < len(arr):
        output.append(arr[right]**2)
        right += 1
    return output