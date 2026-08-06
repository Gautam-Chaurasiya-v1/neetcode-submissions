class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()

        for i in range(n-2):
            mp = defaultdict(int)
            
            for j in range(i+1,n,1):
                
                tmp = -1 * (nums[i] + nums[j])
                
                if mp[tmp] :
                   
                    sortedList = sorted([nums[i],nums[j],tmp])
                    ans.add(tuple(sortedList))
                mp[nums[j]] = 1
        
        return list(ans)

