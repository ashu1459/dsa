class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # [1,2,3,.....,max(piles)]
        res = r

        '''
        Algo:
        - max bananas per hour = maximum value of pile
        - min bananasper hour = 1
        - From 1 to max(piles), do binary search to find out 
          a suitable number which when divided with each piles 
          and then summing all those values gives a total/near of h hours. 
        '''

        while l <= r:
            hours = 0
            mid = l + ((r-l) // 2)

            for p in piles:
                # alternative to math.ceil()
                hours += -(-p // mid)
            
            if hours <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res
