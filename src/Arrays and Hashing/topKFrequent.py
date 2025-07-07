# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.

# Time Complexity: O(n), Space Complexity: O(n)

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freq = {}
    buckets = [[] for _ in range(len(nums) + 1)]
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for element, frequency in freq:
        buckets[frequency].append(element)
    
    res = []
    for i in range(len(buckets) - 1, -1, -1):
        for num in buckets[i]:
            res.append(num)
            if len(res) == k:
                return res

            
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     freq = {}
    #     for num in nums:
    #         freq[num] = freq.get(num, 0) + 1

    #     arr = []
    #     for num, cnt in freq.items():
    #         arr.append([cnt, num])
    #     arr.sort(reverse=True)

    #     res = []
    #     for i in range(k):
    #         res.append(arr[i][1])
    #     return res



            

    #    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     freq = {} # key is integer in nums; value is frequency of said integer
    #     for num in nums:
    #         if num in freq:
    #             freq[num] += 1
    #         else:
    #             freq[num] = 1
        
    #     buckets = [[] for _ in range(len(nums))]
    #     for key,val in freq.items():
    #         buckets[val].append(key)
        
    #     res = []
    #     for i in range(len(buckets) - 1, 0, -1):
    #         for num in buckets[i]:
    #             res.append(num)
    #             if len(res) == k:
    #                 return res

