# Given a string s, find the length of the longest substring without duplicate characters.

def lengthOfLongestSubstring(self, s: str) -> int:
    charSet = set()
    l = 0
    res = 0
    for i in range(len(s)):
        while s[i] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[i]) 
        res = max(res, i - l + 1)
    return res



    # maxCount = 0
    # for i in range(len(s)):
    #     charSet = set()
    #     count = 0
    #     for j in range(i, len(s)):
    #         if s[j] in charSet:
    #             break
    #         charSet.add(s[j])
    #         count += 1
    #     if count > maxCount:
    #         maxCount = count
    # return maxCount


            
            

