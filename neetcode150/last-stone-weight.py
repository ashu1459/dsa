class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # creating maxHeap by reversing the numbers to create a minHeap with Negative Nums as python does not have maxHeap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            bigStone = -1 * heapq.heappop(stones)
            smallStone = -1 * heapq.heappop(stones)
            remainingStone = bigStone - smallStone

            if remainingStone > 0:
                # store reverse/negative of remaining 
                heapq.heappush(stones, 0 - remainingStone)

        return abs(stones[0]) if len(stones) > 0 else 0

        