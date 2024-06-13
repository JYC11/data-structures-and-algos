def duplicateZeros(arr):
    temp = []
    for i in arr:
        if i == 0:
            temp.append(i)
        temp.append(i)
    answer = temp[: len(arr)]
    for i in range(len(arr)):
        arr[i] = answer[i]
    return


duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0])
