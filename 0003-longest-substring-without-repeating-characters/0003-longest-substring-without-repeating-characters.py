class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        max_len = 0
        substring = deque([])

        for i in range(len(s)):
            if substring and s[i] in substring:
                max_len = max(max_len, len(substring))
                while s[i] in substring:
                    substring.popleft()
            substring.append(s[i])
        
        max_len = max(max_len, len(substring))
        return max_len
                
        