class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*(len(nums))

        prefix=1
        postfix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        # last one was the correct multiple
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        # first one was the correct multiple
        # both together wins
        return res
        