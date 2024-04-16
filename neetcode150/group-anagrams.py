class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for string in strs:
            sorted_str = ''.join(sorted(string))

            # Solution-1
            hashMap.setdefault(sorted_str, []).append(string)

            # Solution-2 - expanded version of Solution-1
            # hashMap.setdefault(sorted_str, [])
            # hashMap[sorted_str].append(string)

            # Solution-3
            # hashMap.setdefault(sorted_str, []).extend([string])

        return hashMap.values()