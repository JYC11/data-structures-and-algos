def heightChecker(heights):
    count = 0
    sorted_heights = sorted(heights)
    for i in range(len(heights)):
        if heights[i] != sorted_heights[i]:
            count += 1
    return count
