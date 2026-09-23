class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        x=list(d.items())
        x.sort(key=lambda a:a[1] ,reverse=True)
        an=""
        for i,j in x:
            an+=i*j
        return(an)