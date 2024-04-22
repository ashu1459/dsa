class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(n1):
            res = parent[n1]
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]

            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            print(n1,  p1, n2, p2)
            if p1 == p2:
                return True
            
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += 1
            else:
                parent[p2] = p1
                rank[p1] += 1

            return False
        
        for n1, n2 in edges:
            if union(n1, n2):
                return [n1, n2]