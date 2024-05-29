class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = strs[0]
        for i in range(1, len(strs)):
            temp = ""
            if len(answer) > len(strs[i]):
                length = len(strs[i])
            else:
                length = len(answer)
            for j in range(length):
                if answer[j] == strs[i][j]:
                    temp += answer[j]
                else:
                    break
            answer = temp

        return answer