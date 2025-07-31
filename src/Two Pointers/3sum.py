# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    s = sorted(nums)
    for i in range(len(s)):
        if s[i] > 0:
            break

        if i > 0 and s[i] == s[i - 1]:
            continue

        l = i + 1
        r = len(s) - 1
        while l < r:
            sum = s[l] + s[r] + s[i]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                res.append([s[i], s[l], s[r]])
                l += 1
                r -= 1
                while s[l] == s[l - 1] and l < r:
                    l += 1
    return res
