# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the 
# elements of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Single array usage:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        for j in range(len(nums) - 1, -1, -1):
            res[j] *= suffix
            suffix *= nums[j]
        return res


# 2 array usage:
# def productExceptSelf(self, nums: List[int]) -> List[int]:
#     prefixProds = [0] * len(nums) # [1, 1, 2, 6]
#     suffixProds = [0] * len(nums) # [24, 12, 4, 1]

#     prefix = 1
#     suffix = 1
#     for i in range(len(nums)):
#         prefixProds[i] = prefix
#         prefix *= nums[i]
#     for j in range(len(nums) - 1, -1, -1):
#         suffixProds[j] = suffix
#         suffix *= nums[j]
#     res = []
#     for i in range(len(nums)):
#         res[i] = prefixProds[i] * suffixProds[i]
#     return res



# If division is allowed:
#   def productExceptSelf(self, nums: List[int]) -> List[int]:
#       total_prod = 1
#       for num in nums:
#           total_prod *= num
#       res = []
#       for i, num in enumerate(nums):
#           res[i] = total_prod / num
#       return res

# O(n^2) solution
# def productExceptSelf(self, nums: List[int]) -> List[int]:
#     prod = 1
#     res = [0] * len(nums)
#     for i in range(len(nums)):
#         for j, num in enumerate(nums):
#             if i != j:
#                 prod *= num
#         res[i] = prod
#     return res



