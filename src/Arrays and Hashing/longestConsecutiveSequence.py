# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# HashSet, O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0 
        store = set()

        for num in nums:
            store.add(num)
        
        for num in store:
            if num - 1 not in store:
                count = 0
                while num + count in store:
                    count += 1
                if count > res:
                    res = count
        return res
                




# Brute Force
# def longestConsecutive(self, nums: List[int]) -> int:
#     res = 0 
#     store = set()

#     for num in nums:
#         store.add(num)
    
#     for num in nums:
#         count = 0
#         while num + count in store:
#             count += 1
#         if count > res:
#             res = count
#     return res



                
        
        



