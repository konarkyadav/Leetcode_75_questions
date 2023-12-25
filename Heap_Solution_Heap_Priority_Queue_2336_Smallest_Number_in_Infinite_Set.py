class SmallestInfiniteSet:

    def __init__(self):
        self.heap = list(range(1, 1001))
        heapq.heapify(self.heap)

    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.heap)
        return smallest

    def addBack(self, num: int) -> None:
        if num not in self.heap:
            heapq.heappush(self.heap, num)
