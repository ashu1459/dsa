class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Solution-1: O(nlogn) due to sort
        # num_count = {}
        # for num in nums:
        #     num_count.setdefault(num, 0)
        #     num_count[num] += 1

        # return dict(sorted(num_count.items(), key = lambda x: x[1], reverse = True)[:k]).keys()


        # Solution-2: O(n)
        numCount = {}
        occurrenceNumberList = [[] for i in range(len(nums) + 1)]

        for num in nums:
            numCount[num] = numCount.get(num, 0) + 1

        for num, occurrenceCount in numCount.items():
            occurrenceNumberList[occurrenceCount].append(num)

        res = [];
        # print(occurrenceNumberList);exit()
        for i in range(len(occurrenceNumberList) - 1, 0, -1):
            for num in occurrenceNumberList[i]:
                res.append(num)

                if (len(res) == k):
                    return res
