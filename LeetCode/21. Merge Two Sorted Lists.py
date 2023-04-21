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
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        if list1 is None and list2 is None:
            return list1
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        prev = None

        left = list1
        right = list2

        if left.val > right.val:
            new_node = ListNode(right.val)
            right = right.next
        else:
            new_node = ListNode(left.val)
            left = left.next

        prev = new_node
        head = new_node
        while left or right:
            if left is None:
                new_node = ListNode(right.val)
                right = right.next
            elif right is None:
                new_node = ListNode(left.val)
                left = left.next
            else:
                if left.val > right.val:
                    new_node = ListNode(right.val)
                    right = right.next
                else:
                    new_node = ListNode(left.val)
                    left = left.next
            prev.next = new_node
            prev = new_node

        return head

        left = list1
        right = list2
        new_node = merge(left, right)

        prev = new_node
        head = new_node
        while left or right:
            new_node = merge(left, right)
            prev.next = new_node
            prev = new_node

        return head


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
    root1 = to_sorted_list([1,2,4])
    # root1 = to_sorted_list([])
    # print(root1)
    root2 = to_sorted_list([1,3,4])
    # print(root2)
    new = Sol.mergeTwoLists(root1, root2)
    print(new)
