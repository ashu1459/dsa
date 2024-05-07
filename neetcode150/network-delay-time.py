class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Solution-1: Dijkstra's Algo: TC - O(E * logV)
        # https://www.youtube.com/watch?v=EFg3u_E6eHU
        # https://www.youtube.com/watch?v=XB4MIexjvY0
        t = 0
        visited = set()
        minHeap = [(0, k)]
        nodeToNeighbor = {i:[] for i in range(n + 1)}

        for u, v, w in times:
            nodeToNeighbor[u].append([v, w])

        while minHeap:
            # get min weight/path value
            path, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            # add node to visited
            visited.add(node)
            t = path

            # BFS
            for nei, wei in nodeToNeighbor[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (wei + path, nei))

        return t if len(visited) == n else -1