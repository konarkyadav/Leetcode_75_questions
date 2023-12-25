class SmallestInfiniteSet:

    def __init__(self):
        self.set = set(range(1, 1001))

    def popSmallest(self) -> int:
        ans = min(self.set)
        self.set.remove(ans)
        return ans

    def addBack(self, num: int) -> None:
        if num not in self.set:
            self.set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)