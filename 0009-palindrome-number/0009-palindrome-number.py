class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x_str = str(x)
        # for i in range(len(x_str) // 2):
        #     if x_str[i] != x_str[-1-i]:
        #         return False
        # return True

        if x < 0 or (x // 10 and x % 10 == 0):
            return False
        
        reverse_num = 0
        while x > reverse_num:
            reverse_num *= 10
            reverse_num += (x % 10)
            x //= 10

        return x == reverse_num or x == (reverse_num // 10)