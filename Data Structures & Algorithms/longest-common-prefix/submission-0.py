class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(string) for string in strs)

        for i in range(min_len):
            for string in strs:
                if string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0][:min_len]   
        