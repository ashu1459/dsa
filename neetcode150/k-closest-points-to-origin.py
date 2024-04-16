class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # hashmap = {}
        # pointsDist = []
        # res = []

        # for point in points:
        #     distance = point[0]**2 + point[1]**2
        #     pointsDist.append(-distance)

        #     # initialize the distance key
        #     if distance not in hashmap:
        #         hashmap[distance] = []
            
        #     hashmap[distance].append(point)
        
        # heapq.heapify(pointsDist)

        # while len(pointsDist) > k:
        #     heapq.heappop(pointsDist)
        
        # pointsDist = set(pointsDist)
        
        # for dist in pointsDist:
        #     res += hashmap[-dist]

        # return res

        # Solution-2: O(n)
        res = []
        minHeap = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)

        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -=1
        
        return res
