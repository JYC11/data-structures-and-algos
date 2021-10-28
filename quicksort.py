
def basic_quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        return basic_quicksort(less) + [pivot] + basic_quicksort(greater)

array = [20,52,44,76,134,649,41,24]

print(quicksort(array))