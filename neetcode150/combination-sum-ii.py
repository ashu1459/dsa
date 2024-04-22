class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()

        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            # decision to include current
            subset.append(candidates[i])
            dfs(i + 1, subset, total + candidates[i])

            # decision NOT to include current
            subset.pop()
            # to remove duplicates, keep moving the pointer to bypass duplicate numbers
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, subset, total)

        dfs(0, [], 0)

        return res
        