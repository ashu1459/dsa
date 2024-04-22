class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.endOfWord = True

    def search(self, word: str) -> bool:

        # def backtrack(node, i):
        #     if word[i] == '.':
        #         # match any node children
        #         for c in node.children:
        #             if i == len(word) - 1:
        #                 if node.children[c].endOfWord:
        #                     return True
        #             elif backtrack(node.children[c], i + 1):
        #                 return True
        #     else:
        #         if word[i] not in node.children:
        #             return False
        #         if i == len(word) - 1:
        #             return node.children[word[i]].endOfWord
        #         return backtrack(node.children[word[i]], i + 1)

        #     return False

        def backtrack(cur, i):

            for j in range(i, len(word)):
                if word[j] == '.':
                    for c in cur.children:
                        if backtrack(cur.children[c], j + 1):
                            return True
                    return False
                else:
                    if word[j] not in cur.children:
                        return False
                    cur = cur.children[word[j]]
            
            return cur.endOfWord

        cur = self.root
        
        return backtrack(cur, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)