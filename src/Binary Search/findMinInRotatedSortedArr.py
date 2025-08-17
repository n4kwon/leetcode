# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
# For example, the array nums = [0,1,2,4,5,6,7] might become:
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0 
        r = len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                return res
            midpoint = l + r // 2
            res = min(res, nums[midpoint])
            if nums[midpoint] >= nums[l]:
                l = midpoint + 1
            else:
                r = midpoint - 1
        return res
