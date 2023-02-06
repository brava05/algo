# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # сначала создаем список из которого потом сделаем связанный
        temp=head
        newList = []
        while temp!=None:
            newList.append(temp.val)
            temp=temp.next

        # making new list nod
        next = None
        listlen = len(newList)
        for i in range(listlen):
            if i+1 == n:
                continue
            val = newList[listlen-i-1]
            new_head = ListNode(val, next)
            next = new_head
        
        return new_head
 
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         h1 = h2 = head
#         while h2 and (h2:= h2.next):
#             if h2: h2 = h2.next;h1= h1.next
#         return h1

if __name__ == "__main__":
    head_list = [1,2,3,4,5]

    next = None
    listlen = len(head_list)
    for i in range(listlen):
        val = head_list[listlen-i-1]
        # print(val)
        head = ListNode(val, next)
        next = head

    sol = Solution()
    res = sol.removeNthFromEnd(head, 2)
    print(res)


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]