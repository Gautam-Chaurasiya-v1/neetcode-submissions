class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        firstInd,secondInd = 0 , n-1

        while(firstInd < secondInd):
            sum = numbers[firstInd] + numbers[secondInd]

            if sum == target :
                return [firstInd+1,secondInd+1]
            
            elif sum > target :
                secondInd-=1
            
            else:
                firstInd+=1
            
        