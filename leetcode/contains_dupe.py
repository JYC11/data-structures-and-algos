def containsDuplicate(nums):
        nums = sorted(nums)
        slow = 0
        fast = slow + 1
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                return True
            slow += 1
            fast += 1
        return False