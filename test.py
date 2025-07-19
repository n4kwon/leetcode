
from collections import defaultdict


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
        
        for j in range(len(nums) - 1, -1, -1):
            res[j] *= suffix
            suffix *= nums[j]
        return res
        
            

    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        longest = 0
        for num in nums:
            seen.add(num)
        
        for num in nums:
            if num - 1 not in seen:
                count = 0
                while num + count in seen:
                    count += 1
                if count > longest:
                    longest = count
        return longest


    



        
            