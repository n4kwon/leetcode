# https://leetcode.com/problems/contains-duplicate/


def containsDuplicate(self, nums: List[int]) -> bool:
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] == nums[j]:
    #             return True
    # return False
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False