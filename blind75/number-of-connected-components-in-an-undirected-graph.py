class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Solution-1: Without using Disjoint Union Find 
        # mappings = {i: [] for i in range(n)}
        # res = 0

        # for n1, n2 in edges:
        #     mappings[n1].append(n2)
        #     mappings[n2].append(n1)

        # def dfs(cur):
        #     if cur in visited:
        #         return
            
        #     visited.add(cur)
        #     if cur in mappings:
        #         for node in mappings[cur]:
        #             dfs(node)
        #         del mappings[cur]

        # for i in range(n):
        #     if i in mappings:
        #         visited = set()
        #         dfs(i)
        #         res += 1 

        # return res

        # Solution-2: Using Disjoint Union Find
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += 1
            else:
                parent[p2] = p1
                rank[p1] += 1
            return 1
        
        for n1, n2 in edges:
            n -= union(n1, n2)
        
        return n
            
