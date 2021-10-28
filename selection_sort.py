array = [2,8,5,3,9,4,1]

def selection_sort(array):
    for i in range(len(array)): #outer loop starts from index 0
        min_index = i
        for j in range(i+1,len(array)): #inner loop starts from index 1
            if array[min_index] > array[j]: #if you find a smaller element in array
                min_index = j #this becomes the new smallest index
        array[i],array[min_index] = array[min_index],array[i] #then you swap the places of the min and first element
    return array

print(selection_sort(array))