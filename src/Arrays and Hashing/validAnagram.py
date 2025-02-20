# https://leetcode.com/problems/valid-anagram/description/

def isAnagram(self, s: str, t: str) -> bool:
    if (len(s) != len(t)):
        return False
    
    s_letters = {}
    t_letters = {}

    for i in range(len(s)):
        s_letters[s[i]] = s_letters.get(s[i], 0) + 1
        t_letters[t[i]] = t_letters.get(t[i], 0) + 1
    
    return s_letters == t_letters