class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Solution-1: Utilizes Topological Sort
        mappings = {i:[] for i in range(numCourses)}
        visited, curVisited, res = set(), set(), []

        def dfs(cur):
            if cur in curVisited:
                return False
            if cur in visited:
                return True

            curVisited.add(cur)
            for pre in mappings[cur]:
                if dfs(pre) == False:
                    return False
            curVisited.remove(cur)
            visited.add(cur)
            res.append(cur)
            
        for crs, prev in prerequisites:
            mappings[crs].append(prev)

        for cur in mappings:
            if dfs(cur) == False:
                return []

        return res
