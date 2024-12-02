class Solution {
    public int myAtoi(String s) {
        String replaceS = s.trim();

        if (replaceS.isEmpty()) { return 0; }
        
        int sign = 1;
        if (replaceS.charAt(0) == '-' || replaceS.charAt(0) == '+') {
            if (replaceS.charAt(0) == '-') {
                sign = -1;
            }
            replaceS = replaceS.substring(1);
        }

        int num = 0;
        for (int i = 0; i < replaceS.length(); i++) {
            char c = replaceS.charAt(i);
            if (!Character.isDigit(c)) {
                break;
            } 
            if (num > (Integer.MAX_VALUE - (c - '0')) / 10) {
                return (sign == 1) ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }

            num = num * 10 + (c - '0');
        }

        num *= sign;
        return num;
    }
}