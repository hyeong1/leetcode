class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> romanIntMap = new HashMap();
        romanIntMap.put('I', 1);
        romanIntMap.put('V', 5);
        romanIntMap.put('X', 10);
        romanIntMap.put('L', 50);
        romanIntMap.put('C', 100);
        romanIntMap.put('D', 500);
        romanIntMap.put('M', 1000);

        int result = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (i != 0) {
                if (s.charAt(i) == 'X' && s.charAt(i-1) == 'I') {
                    result += 9;
                    i--;
                } else if (s.charAt(i) == 'C' && s.charAt(i-1) == 'X') {
                    result += 90;
                    i--;
                } else if (s.charAt(i) == 'M' && s.charAt(i-1) == 'C') {
                    result += 900;
                    i--;
                } else if (s.charAt(i) == 'V' && s.charAt(i-1) == 'I') {
                    result += 4;
                    i--;
                } else if (s.charAt(i) == 'L' && s.charAt(i-1) == 'X') {
                    result += 40;
                    i--;
                } else if (s.charAt(i) == 'D' && s.charAt(i-1) == 'C') {
                    result += 400;
                    i--;
                } else {
                    result += romanIntMap.get(s.charAt(i));   
                }
            } else {
                result += romanIntMap.get(s.charAt(i));
            }
        }
        return result;
    }
}