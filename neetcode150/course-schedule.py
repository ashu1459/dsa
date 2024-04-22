class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping = {i:[] for i in range(numCourses)}
        visitSet = set()
        
        for prerequisite in prerequisites:
            mapping[prerequisite[0]].append(prerequisite[1])                    

        def dfs(cur):
            if cur in visitSet:
                return False
            
            visitSet.add(cur)
            while mapping[cur]:
                parent = mapping[cur].pop(0)
                if not dfs(parent):
                    return False
            visitSet.remove(cur)
            
            return True            

        for cur in mapping:
            if mapping[cur]:
                if not dfs(cur):
                    return False
        
        return True