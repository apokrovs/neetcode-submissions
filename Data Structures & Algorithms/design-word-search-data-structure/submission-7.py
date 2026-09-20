class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.end = True

    def search(self, word: str) -> bool:
        current = self.root
        def dfs(index: int, node: TrieNode) -> bool:
            if index == len(word):
                return node.end == True
            if word[index] != ".":
                if word[index] in node.children:
                    return dfs(index+1, node.children[word[index]])
                else:
                    return False
            else:
                res = False
                for c in node.children:
                    res |= dfs(index+1, node.children[c])
                    if res:
                        return True
                return res
                    
        return dfs(0, current)


class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}
        
