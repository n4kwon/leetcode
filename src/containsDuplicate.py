# https://leetcode.com/problems/contains-duplicate/


def containsDuplicate(self, nums: List[int]) -> bool:
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] == nums[j]:
    #             return True
    # return False
    seen = set()
    for i in nums:
        if i in visited:
            return True
        else:
            seen.add(i)
    return False