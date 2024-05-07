class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # Solution-1: Prim's Algo
        # MST problem
        # Prim algorithm is better for this problem, because the graph here is a complete graph. Kruscal is generally optimal for sparse graph.
        res = 0
        N = len(points)
        visitedCount = 0
        visited = [False] * N
        minHeap = [[0, 0]] # Frontier [dist to node, node]
        minCosts = [float("inf")] * N

        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if visited[node]:
                continue

            res += cost
            visitedCount += 1
            visited[node] = True
            
            if visitedCount == N:
                break

            for i in range(N):
                # only unseen nodes to be processed
                if not visited[i]:
                    dist = abs(points[node][0] - points[i][0]) + abs(points[node][1] - points[i][1])
                    # update minHeap and dist only if its less than before
                    if minCosts[i] > dist:
                        minCosts[i] = dist
                        heapq.heappush(minHeap, [dist, i])
        return res
