# https://leetcode.com/problems/koko-eating-bananas/

# we search from min speed of 1 to the maximum possible speed, which is the max amount of bananas in a pile
# (We can't go any slower since a speed of 0 is useless and a higher speed is also useless since we are already eating a 
# pile in one hour anyways). We then perform a binary search on these speeds and if we eat all bananas in an acceptable time,
#  we want to optimize it for a lower eating speed so we update our right hand value to be the valid value we 
# just processed. Conversely, if we take too long to eat the bananas, then we need to eat faster, so we update our 
# slowest speed value to be above the middle speed. Through our iterations, we'll end up with l == r.


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        
        while l < r:
            mid = (l + r) // 2
            curr_hours = 0
            for i in range(len(piles)):
                pile_hours = math.ceil(piles[i] / mid)
                curr_hours += pile_hours
            if curr_hours <= h:
                r = mid
            elif curr_hours > h:
                l = mid + 1
        return r