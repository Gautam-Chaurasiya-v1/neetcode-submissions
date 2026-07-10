class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNum = defaultdict(int) # default to 0

        for num in nums:
            countNum[num] += 1

        print(countNum)
        
        # sortedOrder = sorted(countNum.items(),key=itemgetter(1),reverse=True)

        sortedOrder = sorted(countNum.items() , key = lambda item : item[1],reverse=True)

        result = []

        for i in range(k):
            result.append(sortedOrder[i][0])

 

        return result