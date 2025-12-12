class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]: # front half of array is sorted
                if nums[l] > target or nums[mid] < target: # target is outside of front half
                    l = mid + 1
                else:
                    r = mid - 1
            else: # back half of array is sorted
                if nums[r] < target or nums[mid] < target: # target is outside of back half
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
