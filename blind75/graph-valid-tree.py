class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mappings = {i:[] for i in range(n)}
        visited = set()

        for cur, child in edges:
            if cur > child:
                child, cur = cur, child
            mappings[cur].append(child)
        
        def dfs(cur):
            if cur in visited:
                return False
            
            visited.add(cur)
            for child in mappings[cur]:
                if not dfs(child):
                    return False
            
            return True

        return dfs(0) and len(visited) == n