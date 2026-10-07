class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=[]
        for i in candies:
            l.append(i+extraCandies)
        ma=max(candies)
        j=[]
        for i in l:
            if(i>=ma):
                j.append(True)
            else:
                j.append(False)
        return(j)