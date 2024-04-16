class TimeMap:

    def __init__(self):
        self.ds = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.ds:
            self.ds[key] = []
        self.ds[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:

        res = ""

        if key in self.ds:
            l, r = 0, len(self.ds[key]) - 1

            while l <= r:
                mid = (l + r) // 2

                if timestamp == self.ds[key][mid][0]:
                    return self.ds[key][mid][1]
                elif timestamp > self.ds[key][mid][0]:
                    res = self.ds[key][l][1]
                    l = mid + 1
                else:
                    r = mid - 1

        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)