class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashNum = {}

        for index in range(len(nums)):
            rem = target - nums[index]
        

            # if hashNum.get(rem,-1) != -1:
            if rem in hashNum:
                return [hashNum.get(rem),index]
            
            hashNum[nums[index]] = index
        
        return []