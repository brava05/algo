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
    def deleteDuplicates(self, head) -> ListNode:
        if head is None:
            return head

        dummy = ListNode(0)
        dummy.next = head

        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
            head = head.next

        return dummy.next


    def deleteDuplicates_leet(self, head):
        dummy = pre =ListNode(0)
        # pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next

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
    root1 = to_sorted_list([1, 2, 3, 3, 4, 4, 5])
    new = Sol.deleteDuplicates_leet(root1)
    print(new)
    # print(Sol.deleteDuplicates(to_sorted_list([1, 1, 1, 2, 3])))
