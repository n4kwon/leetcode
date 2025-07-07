# Design an algorithm to encode a list of strings to a string. 
# The encoded string is then sent over the network and is decoded back to the original list of strings.


class Codec:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s) -> List[str]:
        l = 0
        j = 0
        res = []
        while l < len(s):
            while s[j] != '#':
                j += 1
            length = int(s[l : j])
            word = s[j + 1: j + length + 1]
            res.append(word)
            j = j + length + 1
            l = j
        return res



