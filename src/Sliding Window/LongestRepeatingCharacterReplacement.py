# You are given a string s and an integer k. 
# You can choose any character of the string and change it to any other uppercase 
# English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get 
# after performing the above operations.

def characterReplacement(self, s: str, k: int) -> int:
    l = 0
    frequency = {}
    res = 0
    for i in len(s):
        if s[i] in frequency:
            frequency[s[i]] += 1
        else:
            frequency[s[i]] = 0
        if i - l + 1 - max(frequency.values()) <= k:
            res = max(res, i - l + 1)
        else:
            frequency[s[l]] -= 1
            # if not frequency[s[l]]:
            #     frequency.pop(s[l])
            l += 1
    return res