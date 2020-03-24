package Leetcode;

public class L19 {
    public static void main(String[] args)
    {
        Solution_19 solution19 = new Solution_19();
    }
}


// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;

    ListNode(int x) { val = x; }
 }

class Solution_19 {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode temp = new ListNode(0);
        temp.next = head;

        ListNode fast = temp;
        ListNode slow = temp;

        for (int i = 0; i < n; i++)
        {
            fast = fast.next;
        }

        while (fast.next != null)
        {
            fast = fast.next;
            slow = slow.next;
        }

        slow.next = slow.next.next;

        return temp.next;
    }
}
