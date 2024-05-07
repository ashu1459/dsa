class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Solution: Bellman Ford Alo: TC O(E * k)
        prices = [float("inf")] * n
        prices[src] = 0
        
        for i in range(k + 1):
            # make a copy because we need original prices for comparison
            tempP = prices.copy()

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                
                # if total price is less than before, update the price
                if prices[s] + p < tempP[d]:
                    tempP[d] = prices[s] + p

            # update the new prices obtained with this iteration to the original array
            prices = tempP

        return -1 if prices[dst] == float("inf") else prices[dst]

            