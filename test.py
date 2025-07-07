
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # key is integer in nums; value is frequency of said integer
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        buckets = [[] for _ in range(len(nums))]
        for key,val in freq.items():
            buckets[val].append(key)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

        
            


    



        
            