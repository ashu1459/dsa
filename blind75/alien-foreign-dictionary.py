class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minL = min(len(w1), len(w2))
            # heck constraints: incorrect order [kisabc, kis], Correct: [kis, kisabc]
            if len(w1) > len(w2) and w1[:minL] == w2[:minL]:
                return ""
            for j in range(minL):
                # break and log the first different char in both words
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        res = []
        visited = {} # False=visited, True=current_path 

        # DFS with post order Traversal
        def dfs(c):
            if c in visited:
                return visited[c]
            
            visited[c] = True
            # traverse further to check if there's no cycle
            for nei in adj[c]:
                if dfs(nei):
                    # cycle found
                    return True
            visited[c] = False

            res.append(c)

        for c in adj:
            if dfs(c): # cycle found
                return ""
        
        res.reverse()
        return ''.join(res)

        