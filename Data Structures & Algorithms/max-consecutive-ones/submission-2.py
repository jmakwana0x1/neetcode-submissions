class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max=0
        total=0
        for num in nums:
            if num!=1:
                total=0;
            elif num==1:
                total+=1
                if total>max:
                    max=total
        return max;
