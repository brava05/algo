class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self) -> str:
        return f"val: {self.val}, left: {self.left}, right: {self.right}, next: {self.next}"

    def __str__(self) -> str:
        return str(self.val)


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        from collections import deque

        if not root:
            return None

        q = deque([root])
        while q:
            rightNode = None
            for _ in range(len(q)):
                cur = q.popleft()
                cur.next, rightNode = rightNode, cur
                if cur.right:
                    q.extend([cur.right, cur.left])
        return root

    def connect2(self, root):
        if not root:
            return None
        L, R, N = root.left, root.right, root.next
        if L:
            L.next = R
            if N:
                R.next = N.left
            self.connect(L)
            self.connect(R)
        return root

def to_binary_tree(items: list[int]) -> Node:
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> Node:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = Node(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


Sol = Solution()
root1 = to_binary_tree([1,2,3,4,5,6,7])

print(repr(Sol.connect(root1)))