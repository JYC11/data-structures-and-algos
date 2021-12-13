import sys

N = int(sys.stdin.readline())
nums1 = list(map(int,sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline())
nums2 = list(map(int,sys.stdin.readline().strip().split()))

# N = 5
# nums1 = [4, 1, 5, 2, 3]
# M = 5
# nums2 = [1, 3, 7, 9, 5]

nums1.sort()

def binary_search(array,target):
    low = 0
    high = len(array)-1

    while low <= high:
        mid = (low + high)//2
        if array[mid] == target:
            return 1
        if array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return 0

for nums in nums2:
    print(binary_search(nums1,nums))