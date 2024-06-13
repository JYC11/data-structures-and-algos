class Solution:  # array
    def searchInsert(self, nums, target):
        target_arr = nums + [target]
        target_arr = list(set(target_arr))
        target_arr.sort()
        low = 0
        high = len(target_arr) - 1
        idx = self.binarySearch(target_arr, low, high, target)
        return idx

    def binarySearch(self, nums, low, high, target):
        if low > high:
            return None
        else:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return self.binarySearch(nums, low, mid - 1, target)
            else:
                return self.binarySearch(nums, mid + 1, high, target)
        return None


s = Solution()

s.searchInsert([1, 3, 5, 6], 5)
