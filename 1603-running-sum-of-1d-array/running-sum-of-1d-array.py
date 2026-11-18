class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        l=[]
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            l.append(sum)
        return(l)