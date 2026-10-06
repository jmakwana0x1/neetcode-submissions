class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        # collect numbers and it's frquency
        for num in nums:
            count[num]=1+count.get(num,0)
        # create heap from the keys push and only keep top k 
        heap=[]
        for num in count.keys():
            heapq.heappush(heap,(count[num],num))
            if len(heap)>k:
                heapq.heappop(heap)
        # take only the second element from the heapq w
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        