class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, subset, subsetSum):
            if subsetSum == target:
                res.append(subset.copy())
                return
            elif i >= len(candidates) or subsetSum > target:
                return

            subset.append(candidates[i])
            dfs(i, subset, subsetSum + candidates[i])

            subset.pop()
            dfs(i+1, subset, subsetSum)

        dfs(0, [], 0)
        return res
        