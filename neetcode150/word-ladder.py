class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        patterns = {}

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                patterns.setdefault(pattern, []).append(word)
        
        visited = set()
        q = [beginWord]
        res = 1
        while q:
            for i in range(len(q)):
                word = q.pop(0)
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for wrd in patterns[pattern]:
                        if wrd not in visited:
                            visited.add(wrd)
                            q.append(wrd)
            res += 1

        return 0