# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     res = defaultdict(list)
    #     for s in strs:
    #         curr = ''.join(sorted(s))
    #         res[curr].append(s)
    #     return list(res.values())
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            res[tuple(freq)].append(s)
        return list(res.values())

                
                

