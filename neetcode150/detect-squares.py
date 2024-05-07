class DetectSquares:

    def __init__(self):
        self.points = []
        self.pointsSet = {}

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.pointsSet[tuple(point)] = self.pointsSet.get(tuple(point), 0) + 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            if (x, py) in self.pointsSet and (px, y) in self.pointsSet:
                res += self.pointsSet[(x, py)] * self.pointsSet[(px, y)]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)