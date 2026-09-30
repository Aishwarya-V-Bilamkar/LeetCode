class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        ma=0
        ans=0
        for i,j in d.items():
            if(j>ma):
                ma=j
                ans=i
        return ans