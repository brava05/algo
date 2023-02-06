# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# for list
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         midTuple = divmod(len(head), 2)
#         mid = midTuple[0] + 1
        
#         return head[mid-1:]


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length=0
        temp=head
        # сначала находим середину списка
        while temp!=None:
            length+=1
            temp=temp.next
        new_node=head
        for i in range(length//2):
            # назначаем головой следующий элемент списка
            new_node=new_node.next
        return new_node

# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         h1 = h2 = head
#         while h2 and (h2:= h2.next):
#             if h2: h2 = h2.next;h1= h1.next
#         return h1

if __name__ == "__main__":
    head_list = [1,2,3,4,5,6]

    next = None
    listlen = len(head_list)
    for i in range(listlen):
        val = head_list[listlen-i-1]
        # print(val)
        head = ListNode(val, next)
        next = head

    sol = Solution()
    res = sol.middleNode(head)
    print(res)


# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.