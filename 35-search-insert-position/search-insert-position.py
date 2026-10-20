class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        fon=False
        for i in range(len(nums)):
            if nums[i] >=target:
                return(i)
                fon=True
                break
        if(fon==False):
            return(len(nums))