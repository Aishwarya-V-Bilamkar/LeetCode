class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        d={}
        for i in nums:
            if(i not in d):
                d[i]=1
            else:
                d[i]+=1
        l=[]
        count=0
        for i,j in d.items():
            if(j>1):
                return True
                break
        return False
            