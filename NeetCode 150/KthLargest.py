class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)

        self.k = k
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]

