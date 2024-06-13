def checkIfExist(arr):
    count = 0
    for i in range(len(arr)):
        temp = arr.copy()
        temp[i] = "_"
        if arr[i] * 2 in temp:
            count += 1
    return count > 0


print(checkIfExist([10, 2, 5, 3]))
print(checkIfExist([7, 1, 14, 11]))
print(checkIfExist([3, 1, 7, 11]))
print(checkIfExist([1, 1, 3, 0]))
print(checkIfExist([0, 0]))
