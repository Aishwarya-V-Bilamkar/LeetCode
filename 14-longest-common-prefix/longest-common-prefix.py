class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        c=""
        min=len(strs[0])
        for i in strs:
            if(len(i)<min):
                min=len(i)
                c+=i
        for i in range(min):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return strs[0][0:i]

        return strs[0][0:min]
            