class Solution:  # hash map
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        distinct = set(nums1 + nums2 + nums3)
        distinct_dict = {}

        for n in distinct:
            if n in nums1:
                distinct_dict[n] = distinct_dict.get(n, 0) + 1
            if n in nums2:
                distinct_dict[n] = distinct_dict.get(n, 0) + 1
            if n in nums3:
                distinct_dict[n] = distinct_dict.get(n, 0) + 1

        at_least_two = [k for k, v in distinct_dict.items() if v > 1]
        return at_least_two
