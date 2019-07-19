'''
The k-th node of a linkedlist from the back
leetcode 19
'''

# slow and fast pointer
def solution1(head, n):
    node1 = head
    node2 = head
    for _ in range(n):
        node2 = node2.next

    if not node2:
        head = head.next
    else:
        while node2.next:
            node2 = node2.next
            node1 = node1.next

        node1.next = node1.next.next

    return head

# move the elements before n
def solution2(head, n):
    def index(node):
        if not node:
            return 0

        i = index(node.next) + 1
        if i > n:
            node.next.val = node.val
        return i

    index(head)
    return head.next

def solution3(head, n):
    def remove(head):
        if not head:
            return 0, head

        i, head.next = remove(head.next)

        return i + 1, [head, head.next][i+1==n]

    return remove(head)[1]




