class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjacencyList = {src:[] for src, dest in tickets}

        for src, dest in tickets:
            adjacencyList[src].append(dest)

        for key in adjacencyList:
            adjacencyList[key].sort()

        # Solution-1: Working but slow - https://www.youtube.com/watch?v=iwUJeJ8BZM4
        # def hierholzerAlgo(node):
        #     if node not in adjacencyList:
        #         if len(path) == len(tickets) + 1:
        #             return True
        #         return False
        #     if not adjacencyList[node]:
        #         return True
            
        #     while adjacencyList[node]:
        #         dest = adjacencyList[node].pop(0)
        #         path.append(dest)
        #         if hierholzerAlgo(dest) == False:
        #             adjacencyList[node].append(dest)
        #             path.pop()

        # path = ['JFK']
        # hierholzerAlgo('JFK')
        # return path

        # Solution-2: using DFS
        def dfs(node, res):
            if node in adjacencyList:
                while adjacencyList[node]:
                    dest = adjacencyList[node].pop(0)
                    dfs(dest, res)
            res.append(node)
        
        res = []
        dfs('JFK', res)
        return res[::-1]