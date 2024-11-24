/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        String num1 = "";
        String num2 = "";

        ListNode l1_curr = l1;
        while (l1_curr != null) {
            num1 += String.valueOf(l1_curr.val);
            l1_curr = l1_curr.next;
        }
        ListNode l2_curr = l2;
        while (l2_curr != null) {
            num2 += String.valueOf(l2_curr.val);
            l2_curr = l2_curr.next;
        }

        StringBuffer sb1 = new StringBuffer(num1);
        StringBuffer sb2 = new StringBuffer(num2);
        String sum = String.valueOf(Integer.parseInt(sb1.reverse().toString()) + Integer.parseInt(sb2.reverse().toString()));

        ListNode res = new ListNode(Character.getNumericValue(sum.charAt(sum.length() - 1)));
        ListNode curr = res;
        for (int i = sum.length() - 2; i >= 0; i--) {
            curr.next = new ListNode(Character.getNumericValue(sum.charAt(i)));
            curr = curr.next;
        }

        return res;
    }
}