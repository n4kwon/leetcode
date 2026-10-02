class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word) -> bool: # checks if exact word exists in trie
        curr = self
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord

    def startsWith(self, prefix) -> bool:
        curr = self
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

    def deleteWord(self, word) -> bool:
        return self._canDelete(self, word, 0)

    # 
    def _canDelete(self, curr, word, idx):
        if idx == len(word):
            if not curr.endOfWord:
                return False
            curr.endOfWord = False
            return len(curr.children) == 0

        ch = word[idx]
        if ch not in curr.children:
            return False

        canDelete = self._canDelete(curr.children[ch], word, idx + 1)
        if canDelete:
            del curr.children[ch]
            return not curr.endOfWord and len(curr.children) == 0
        return False