class Solution {
    public String intToRoman(int num) {
        HashMap<Integer, Character> map = new HashMap<Integer, Character>();
        map.put(1, 'I');
        map.put(5, 'V');
        map.put(10, 'X');
        map.put(50, 'L');
        map.put(100, 'C');
        map.put(500, 'D');
        map.put(1000, 'M');

        int squareTen = 1;
        String result = "";
        while (num != 0) {
            int n = num % 10 ;
            if (n == 0) {
                num /= 10;
                squareTen *= 10;
                continue;
            }
            if (n < 4) {
                for (int i = 0; i < n; i++) {
                    result = map.get(squareTen) + result;
                }
            } else if (n == 4) {
                String temp = "";
                temp += map.get(squareTen);
                temp += map.get(squareTen * 5);
                result = temp + result;
            } else if (4 < n && n < 9) {
                String temp = "";
                temp += map.get(squareTen * 5);
                for (int i = 0; i < (n - 5); i++) {
                    temp += map.get(squareTen);
                } 
                result = temp + result;
            } else if (n == 9) {
                String temp = "";
                temp += map.get(squareTen);
                temp += map.get(squareTen * 10);
                result = temp + result;
            }
            num /= 10;
            squareTen *= 10;
        } 
        return result;
    }
}