class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # answer = strs[0]
        # for i in range(1, len(strs)):
        #     temp = ""
        #     for j in range(min(len(strs[i]), len(answer))):
        #         if answer[j] == strs[i][j]:
        #             temp += answer[j]
        #         else:
        #             break
        #     answer = temp

        # # answer = ""
        # # strs = sorted(strs)
        # # first = strs[0]
        # # last = strs[-1]
        # # for i in range(min(len(first), len(last))):
        # #     if first[i] != last[i]:
        # #         return answer
        # #     else:
        # #         answer += first[i]
        # return answer
        mini,maxi=min(strs),max(strs)
        print(mini, maxi)
        for i in range(len(mini)):
            if mini[i]!=maxi[i]:
                return mini[:i]
        return mini