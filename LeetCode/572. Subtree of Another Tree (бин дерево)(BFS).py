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


class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        if self.same(root, subRoot):
            return True

        if not root:
            return False

        if self.isSubtree(root.left, subRoot):
            return True

        if self.isSubtree(root.right, subRoot):
            return True

        return False

    def same(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val != right.val:
            return False

        if self.same(left.left, right.left) and self.same(left.right, right.right):
            return True

        return False


if __name__ == '__main__':
    Sol = Solution()

    root1 = to_binary_tree([3, 4, 5, 1, 2])
    subRoot = to_binary_tree([4, 1, 2])
    print(Sol.isSubtree(root1, subRoot))

    root1 = to_binary_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    subRoot = to_binary_tree([4, 1, 2])
    print(Sol.isSubtree(root1, subRoot))
