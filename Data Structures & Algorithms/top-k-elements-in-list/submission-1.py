class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num,0) + 1

        heap = []
        for num,cnt in count.items():
            heapq.heappush(heap,(cnt,num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for num in heap:
            res.append(num[1])

        return res