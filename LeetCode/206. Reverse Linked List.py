# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        node = self
        res = str(node.val)
        while node.next:
            node = node.next
            res = res + ' ' + str(node.val)
        return res

class Solution:
    def reverseList_leet(self, head) -> ListNode:
        if head is None:
            return head
        prev = None
        cur = head
        next = None

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev

    def reverseList_my(self, head) -> ListNode:
        if head is None:
            return head
        new_list = []
        cur = head
        while True:
            new_list.append(cur.val)

            if cur.next is None:
                break
            cur = cur.next

        new_list.reverse()
        print(new_list)
        return to_sorted_list(new_list)


def to_sorted_list(list1):
    n = len(list1)
    if n == 0:
        return None

    new_node = ListNode(list1[0])
    head = new_node
    prev = new_node
    for i in range(1, n):
        new_node = ListNode(list1[i])
        prev.next = new_node
        prev = new_node

    return head


if __name__ == "__main__":
    Sol = Solution()
    root1 = to_sorted_list([1, 2, 3, 4, 5])
    new = Sol.reverseList_leet(root1)
    print(new)
