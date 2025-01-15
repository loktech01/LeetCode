import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mn_heap = []
        for num in nums:
            heapq.heappush(mn_heap,num)
            if len(mn_heap) > k:
                heapq.heappop(mn_heap)
        return mn_heap[0]