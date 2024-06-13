def smallest_gte_s(arr, s):
    min_size = float("inf")
    start = 0
    curr_sum = 0
    for end, val in enumerate(arr):
        curr_sum += val
        while curr_sum >= s:
            min_size = min(min_size, end - start + 1)
            curr_sum -= arr[start]
            start += 1
    return min_size


print(smallest_gte_s([1, 3, 2, 5, 4], 9))
