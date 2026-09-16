class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c in current.chars:
                current = current.chars[c]
            else:
                current.chars[c] = TrieNode()
                current = current.chars[c]
        current.is_end = True


    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c in current.chars:
                current = current.chars[c]
                continue
            else:
                return False
        if current.is_end == True:
            return True
        else:
            return False
  

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c in current.chars:
                current = current.chars[c]
                continue
            else:
                return False
        return True


class TrieNode:
    def __init__(self):
        self.is_end = False
        self.chars = {}
        
        