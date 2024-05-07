class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hashmap = {}
        for h in hand:
            hashmap[h] = hashmap.get(h, 0) + 1

        # Solution-2: TC nLogn
        # heapq.heapify(hand)
        # while hand:
        #     smallest = heapq.heappop(hand)
            
        #     if hashmap[smallest] == 0:
        #         continue

        #     for i in range(groupSize):
        #         if smallest in hashmap and hashmap[smallest] > 0:
        #             hashmap[smallest] -= 1
        #         else:
        #             return False

        #         smallest += 1

        # Solution-2: Neetcode approach TC - nlogn
        hand = list(hashmap.keys())
        heapq.heapify(hand)
        while hand:
            smallest = hand[0]

            for i in range(smallest, smallest + groupSize):
                if i not in hashmap:
                    return False

                hashmap[i] -= 1

                if hashmap[i] == 0:
                    if i != hand[0]:
                        return False
                    heapq.heappop(hand)

        return True