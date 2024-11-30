class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1) {
            return s;
        }

        List<List<Character>> zigzag = new ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            zigzag.add(new ArrayList<>());
        }

        int cycle = (2 * numRows) - 2;
        for (int i = 0; i < s.length(); i++) {
            int row = i % cycle;
            if (row >= numRows) {
                row = cycle - row;
            }
            zigzag.get(row).add(s.charAt(i));
        }

        StringBuilder sb = new StringBuilder();
        for (List<Character> row : zigzag) {
            for (char c : row) {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}