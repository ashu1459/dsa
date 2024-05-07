class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashset = {}

        for i in range(len(s)):
            hashset[s[i]] = i
        
        size, end, res = 0, 0, []
        for j in range(len(s)):
            size += 1
            end = max(end, hashset[s[j]])
                
            if end == j:
                res.append(size)
                size = 0

        return res