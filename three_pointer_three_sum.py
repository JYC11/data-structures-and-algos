def three_sum(arr, target):
    left = 1
    right = len(arr) - 1

    for i in range(len(arr)):
        if arr[i] + arr[left] + arr[right] < target:
            left += 1
        elif arr[i] + arr[left] + arr[right] > target:
            right -= 1
        else:
            return [i,left, right]
    
    return [-1,-1,-1]