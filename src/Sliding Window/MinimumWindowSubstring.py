# Given two strings s and t of lengths m and n respectively, 
# return the minimum window substring of s such that every character in t 
# (including duplicates) is included in the window. 
# If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        target = {} # dictionary that tracks characters in t
        window = {}
        included = 0
        res = [-1, -1]
        resLen = float("infinity")
        # first fill up the target dictionary
        for c in t:
            target[c] = target.get(c, 0) + 1
        
        for i in range(len(s)):
            window[s[i]] = window.get(s[i], 0) + 1
            # check if we have required frequency of character in window
            if window[s[i]] == target.get(s[i], 0): 
                included += 1
            while included == len(target.keys()): 
                # keep iterating for smallest window possible by incrementing left pointer
                if resLen > i - l + 1:
                    res = [l, i]
                    resLen = i - l + 1
                window[s[l]] -= 1
                if (window[s[l]] < target.get(s[l], 0)):
                    included -= 1
                l += 1
        l, r = res
        if resLen != float("infinity"):
            return s[l : r + 1]
        else:
            return "" 
        

